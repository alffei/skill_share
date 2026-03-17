#!/usr/bin/env python3
"""
Environment Setup for NotebookLM Skill
Manages virtual environment and dependencies automatically
"""

import os
import sys
import subprocess
import venv
from pathlib import Path


class SkillEnvironment:
    """Manages skill-specific virtual environment"""

    READY_MARKER_NAME = ".notebooklm-skill-ready"
    REQUIRED_IMPORTS = (
        "from patchright.sync_api import sync_playwright",
        "from dotenv import load_dotenv",
    )

    def __init__(self):
        # Skill directory paths
        self.skill_dir = Path(__file__).parent.parent
        self.venv_dir = self.skill_dir / ".venv"
        self.requirements_file = self.skill_dir / "requirements.txt"
        self.ready_marker = self.venv_dir / self.READY_MARKER_NAME

        # Python executable in venv
        if os.name == 'nt':  # Windows
            self.venv_python = self.venv_dir / "Scripts" / "python.exe"
            self.venv_pip = self.venv_dir / "Scripts" / "pip.exe"
        else:  # Unix/Linux/Mac
            self.venv_python = self.venv_dir / "bin" / "python"
            self.venv_pip = self.venv_dir / "bin" / "pip"

    def ensure_venv(self) -> bool:
        """Ensure virtual environment exists and is set up"""

        # Create venv if it doesn't exist
        if not self.venv_dir.exists():
            print(f"🔧 Creating virtual environment in {self.venv_dir.name}/")
            try:
                venv.create(self.venv_dir, with_pip=True)
                print("✅ Virtual environment created")
            except Exception as e:
                print(f"❌ Failed to create venv: {e}")
                return False
        elif not self.venv_python.exists() or not self.venv_pip.exists():
            print("⚠️ Existing virtual environment is incomplete. Recreating it...")
            self.recreate_venv()
            try:
                venv.create(self.venv_dir, with_pip=True)
                print("✅ Virtual environment recreated")
            except Exception as e:
                print(f"❌ Failed to recreate venv: {e}")
                return False

        if self.is_environment_ready():
            if self.is_in_skill_venv():
                print("✅ Already running in skill virtual environment")
            else:
                print("✅ Skill environment already ready")
            return True

        # Install/update dependencies
        if self.requirements_file.exists():
            print("📦 Installing dependencies...")
            try:
                self.remove_ready_marker()
                self.run_pip_install(
                    ["-r", str(self.requirements_file)],
                    description="Python dependencies"
                )
                print("✅ Dependencies installed")

                # Install Chrome for Patchright (not Chromium!)
                # Using real Chrome ensures cross-platform reliability and consistent browser fingerprinting
                # See: https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python#anti-detection
                print("🌐 Installing Google Chrome for Patchright...")
                try:
                    self.run_subprocess(
                        [str(self.venv_python), "-m", "patchright", "install", "chrome"],
                        check=True,
                        description="Patchright Chrome runtime"
                    )
                    print("✅ Chrome installed")
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Warning: Failed to install Chrome: {e}")
                    print("   You may need to run manually: python -m patchright install chrome")
                    print("   Chrome is required (not Chromium) for reliability!")

                self.write_ready_marker()
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install dependencies: {e}")
                self.print_dependency_help()
                return False
        else:
            print("⚠️ No requirements.txt found, skipping dependency installation")
            self.write_ready_marker()
            return True

    def is_in_skill_venv(self) -> bool:
        """Check if we're already running in the skill's venv"""
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            # We're in a venv, check if it's ours
            venv_path = Path(sys.prefix)
            return venv_path == self.venv_dir
        return False

    def get_python_executable(self) -> str:
        """Get the correct Python executable to use"""
        if self.venv_python.exists():
            return str(self.venv_python)
        return sys.executable

    def is_environment_ready(self) -> bool:
        """Check whether the venv and required packages are usable"""
        if not self.venv_python.exists() or not self.venv_pip.exists():
            return False

        if not self.has_required_imports():
            return False

        if not self.ready_marker.exists():
            self.write_ready_marker()

        return True

    def has_required_imports(self) -> bool:
        """Check whether the required Python packages can be imported"""
        check_code = "; ".join(self.REQUIRED_IMPORTS)
        result = subprocess.run(
            [str(self.venv_python), "-c", check_code],
            capture_output=True,
            text=True
        )
        return result.returncode == 0

    def recreate_venv(self) -> None:
        """Remove a broken venv before recreating it"""
        import shutil

        shutil.rmtree(self.venv_dir, ignore_errors=True)

    def remove_ready_marker(self) -> None:
        """Clear the ready marker when setup is incomplete"""
        if self.ready_marker.exists():
            self.ready_marker.unlink()

    def write_ready_marker(self) -> None:
        """Write a marker file after setup completes successfully"""
        self.ready_marker.write_text("ready\n")

    def run_subprocess(self, cmd: list, check: bool, description: str) -> subprocess.CompletedProcess:
        """Run a subprocess and stream its output to the terminal"""
        print(f"   -> {description}: {' '.join(cmd)}")
        return subprocess.run(cmd, check=check, text=True)

    def run_pip_install(self, pip_args: list, description: str) -> None:
        """Install packages with visible output and shorter retry windows"""
        retries = os.environ.get("NOTEBOOKLM_PIP_RETRIES", "1")
        timeout = os.environ.get("NOTEBOOKLM_PIP_TIMEOUT", "15")
        index_url = os.environ.get("NOTEBOOKLM_PIP_INDEX_URL") or os.environ.get("PIP_INDEX_URL")

        cmd = [
            str(self.venv_python),
            "-m",
            "pip",
            "--disable-pip-version-check",
            "install",
            "--no-cache-dir",
            "--progress-bar",
            "off",
            "--retries",
            retries,
            "--timeout",
            timeout,
        ]
        if index_url:
            cmd.extend(["-i", index_url])
            print(f"   Using package index: {index_url}")

        cmd.extend(pip_args)
        self.run_subprocess(cmd, check=True, description=description)

    def print_dependency_help(self) -> None:
        """Print actionable hints when dependency installation fails"""
        mirror_url = "https://pypi.tuna.tsinghua.edu.cn/simple"
        print("   Common causes: DNS resolution failure, no outbound network, or a blocked PyPI mirror.")
        print("   If you are in mainland China, try:")
        print(f"   export NOTEBOOKLM_PIP_INDEX_URL={mirror_url}")
        print("   Then rerun: python scripts/run.py auth_manager.py status")
        print("   If setup was interrupted previously, the wrapper will repair the existing .venv on the next run.")

    def run_script(self, script_name: str, args: list = None) -> int:
        """Run a script with the virtual environment"""
        script_path = self.skill_dir / "scripts" / script_name

        if not script_path.exists():
            print(f"❌ Script not found: {script_path}")
            return 1

        # Ensure venv is set up
        if not self.ensure_venv():
            print("❌ Failed to set up environment")
            return 1

        # Build command
        cmd = [str(self.venv_python), str(script_path)]
        if args:
            cmd.extend(args)

        print(f"🚀 Running: {script_name} with venv Python")

        try:
            # Run the script with venv Python
            result = subprocess.run(cmd)
            return result.returncode
        except Exception as e:
            print(f"❌ Failed to run script: {e}")
            return 1

    def activate_instructions(self) -> str:
        """Get instructions for manual activation"""
        if os.name == 'nt':
            activate = self.venv_dir / "Scripts" / "activate.bat"
            return f"Run: {activate}"
        else:
            activate = self.venv_dir / "bin" / "activate"
            return f"Run: source {activate}"


def main():
    """Main entry point for environment setup"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Setup NotebookLM skill environment'
    )

    parser.add_argument(
        '--check',
        action='store_true',
        help='Check if environment is set up'
    )

    parser.add_argument(
        '--run',
        help='Run a script with the venv (e.g., --run ask_question.py)'
    )

    parser.add_argument(
        'args',
        nargs='*',
        help='Arguments to pass to the script'
    )

    args = parser.parse_args()

    env = SkillEnvironment()

    if args.check:
        if env.is_environment_ready():
            print(f"✅ Environment is ready: {env.venv_dir}")
            print(f"   Python: {env.get_python_executable()}")
            print(f"   To activate manually: {env.activate_instructions()}")
        elif env.venv_dir.exists():
            print(f"✅ Virtual environment exists: {env.venv_dir}")
            print("   Status: incomplete setup, rerun setup_environment.py to repair it")
            print(f"   Python: {env.get_python_executable()}")
            print(f"   To activate manually: {env.activate_instructions()}")
        else:
            print(f"❌ No virtual environment found")
            print(f"   Run setup_environment.py to create it")
        return

    if args.run:
        # Run a script with venv
        return env.run_script(args.run, args.args)

    # Default: ensure environment is set up
    if env.ensure_venv():
        print("\n✅ Environment ready!")
        print(f"   Virtual env: {env.venv_dir}")
        print(f"   Python: {env.get_python_executable()}")
        print(f"\nTo activate manually: {env.activate_instructions()}")
        print(f"Or run scripts directly: python setup_environment.py --run script_name.py")
    else:
        print("\n❌ Environment setup failed")
        return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
