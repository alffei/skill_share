# Troubleshooting

## Login setup does not complete

- Run `python scripts/run.py auth_manager.py setup`.
- Keep the browser visible.
- Finish Google login manually.
- If it still fails, clear state and retry:

```bash
python scripts/run.py auth_manager.py clear
python scripts/run.py auth_manager.py setup
```

## Query says not authenticated

- Check auth state:

```bash
python scripts/run.py auth_manager.py status
python scripts/run.py auth_manager.py validate
```

- If validation fails, re-authenticate:

```bash
python scripts/run.py auth_manager.py reauth
```

## Chrome or Patchright install fails

Run the wrapper again first. It bootstraps `.venv` automatically.

If a previous setup was interrupted, rerunning the wrapper will now repair the partial `.venv` instead of treating it as healthy.

If setup partially succeeded, activate the environment and install manually:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m patchright install chrome
```

## Setup appears stuck at "Installing dependencies..."

Recent versions of the wrapper print pip output directly. If it still stops there for a while, the usual cause is network or DNS access to PyPI.

Try a reachable mirror:

```bash
export NOTEBOOKLM_PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
python scripts/run.py auth_manager.py status
```

Optional tuning:

```bash
export NOTEBOOKLM_PIP_TIMEOUT=15
export NOTEBOOKLM_PIP_RETRIES=1
```

If you want to inspect environment state before retrying:

```bash
python scripts/setup_environment.py --check
```

## NotebookLM UI changed and selectors fail

- Re-run the query with `--show-browser`.
- Inspect whether the input box or answer container selectors changed.
- Update selectors in [config.py](../scripts/config.py) if NotebookLM changed its markup.

## Browser state looks corrupted

Preview cleanup:

```bash
python scripts/run.py cleanup_manager.py
```

Clear browser state while keeping the notebook library:

```bash
python scripts/run.py cleanup_manager.py --confirm --preserve-library
```

Then authenticate again:

```bash
python scripts/run.py auth_manager.py setup
```
