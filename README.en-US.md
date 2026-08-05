

# Skill Share 🚀

This is a project dedicated to sharing **Agent Skills**. It primarily includes custom-built skills for personal use, designed to improve the processing efficiency and standardization of AI Agents in specific scenarios.

This repository currently contains skills compatible with both **Antigravity** and **Codex**. You can choose to install them based on your respective runtime environments.

## 📁 Directory Structure

Each skill resides in its own directory, containing the core `SKILL.md` instruction file along with related templates or resources.

```text
.
├── spec-architect/           # Spec Architect Skill
├── ruoyi-code-generator/      # RuoYi Code Generator Skill
├── springboot-init/          # Spring Boot Initialization Skill
├── wechat-operation/         # WeChat Official Account Operation Skill
├── superpowers-antigravity/  # Antigravity Core Capabilities (ported from Superpowers)
├── skill-installer/           # Skill Installer (one-click install/update skills)
├── draw-io/                  # draw-io Diagram Engineering Skill
├── notebooklm-skill-codex/   # Codex Edition NotebookLM Local Retrieval Skill
├── adk-skill-design-patterns-zh/ # 5 AI Agent Skill Design Patterns
└── README.md
```

## 🛠 Included Skills

### 1. [Spec-Architect](./spec-architect/SKILL.md)
**Role**: Professional System Architect
**Core Value**: Rejects "Vibe Coding" (ad-hoc/casual coding) and ensures accurate code implementation through a rigorous Spec workflow.
**Workflow**:
1. **Phase 1: Requirements** - Translates vague ideas into structured requirement documents.
2. **Phase 2: Design** - Generates architecture diagrams, data models, and interface designs based on requirements.
3. **Phase 3: Planning** - Breaks down the design into executable atomic tasks.

### 2. [RuoYi-Code-Generator](./ruoyi-code-generator/SKILL.md)
**Role**: RuoYi Framework Code Generator
**Core Value**: Automatically generates complete CRUD code compliant with RuoYi framework standards based on database table structures, significantly boosting development efficiency.
**Generated Content**:
- **Java Backend**: Domain, Mapper, Service, ServiceImpl, Controller
- **MyBatis**: XML mapping files
- **Vue Frontend**: API wrappers, list page components
- **SQL Scripts**: Menu initialization SQL

**Use Cases**: Creating new modules, adding business features, rapidly generating standard code from table structures.

### 3. [SpringBoot-Init](./springboot-init/SKILL.md)
**Role**: Professional Spring Development Architect
**Core Value**: Rapidly initializes high-standard Spring Boot project skeletons, integrating best practices to avoid reinventing basic infrastructure.
**Key Features**:
- **Rapid Initialization**: Includes `pom.xml`, `application.yml`, and core base classes.
- **Enforced Standards**: Strictly defines data flow (DTO/VO/Entity) and transaction management.
- **Modernization**: Deeply integrates JDK 17+ Records and MyBatis-Plus.
- **Automated Workflow**: Provides standardized operational flows for project initialization and adding business modules.

**Use Cases**: Launching new projects, unifying infrastructure, standardizing monolithic applications.

### 4. [WeChat-Operation](./wechat-operation/README.md)
**Role**: WeChat Official Account Operations Expert
**Core Value**: Covers the entire workflow from account positioning and topic planning to viral content creation, improving operational efficiency for tech-focused accounts.
**Key Features**:
- **Full Workflow Coverage**: Includes 8 sub-skills: positioning, topic selection, titles, outlines, writing, case studies, formatting, and iteration.
- **Standardized Templates**: Each sub-skill comes with mature Prompt templates.
- **Tech-Focused**: Optimized for technology/engineering accounts, rejecting low-quality content.

**Use Cases**: Cold-starting official accounts, creating technical articles, standardizing operational workflows.

### 5. [Superpowers-Antigravity](./superpowers-antigravity/README.md)
**Role**: Senior Software Engineer / Architect
**Core Value**: Ported from the renowned [Superpowers](https://github.com/obra/superpowers), this is a structured software development workflow that significantly improves development success rates by enforcing Agents to follow best engineering practices.
**Key Features**:
- **Systematic Debugging**: Includes advanced debugging skills such as root cause tracing and defensive programming.
- **Standardized Workflow**: Provides slash commands for requirement brainstorming, task breakdown, batch execution, etc.
- **Quality Assurance**: Integrates Test-Driven Development (TDD) and strict pre-completion validation processes.

**Use Cases**: Complex business development, system refactoring, deep bug fixes.

### 6. [Skill-Installer](./skill-installer/README.md)
**Role**: Skill Management Expert
**Core Value**: Simplifies skill discovery and installation, supporting one-click deployment of skills to Antigravity from GitHub repositories or curated lists.
**Key Features**:
- **Multi-Source Support**: Supports installation via GitHub repository URLs or repository paths.
- **Flexible Deployment**: Supports installation to global directories or the current project workspace.
- **Auto-Search**: Supports listing recommended official/community skills.

**Use Cases**: Environment initialization, rapid installation of new tools, cross-project skill synchronization.

### 7. [draw-io](./draw-io/README.md)
**Role**: AI Agent Diagram Engineering Expert
**Core Value**: Enables Agents to manage architecture diagrams like code by directly manipulating XML source files and automatically converting them to high-fidelity PNGs, ensuring diagram quality.
**Key Features**:
- **XML Source Editing**: Agents directly read/write `.drawio` files for pixel-level precision control.
- **Automated Conversion**: Provides automated scripts for one-click generation of 2x resolution, transparent background PNGs.
- **AWS Integration**: Built-in search tool for 600+ official AWS icons to quickly locate service graphics.
- **Professional Standards**: Pre-set design guidelines for fonts, spacing, alignment, etc., ensuring professional output out-of-the-box.

**Use Cases**: Creating architecture diagrams, technical documentation illustrations, AWS solution design, unifying diagram styles.

### 8. [NotebookLM-Skill-Codex](./notebooklm-skill-codex/README.md)
**Role**: Local NotebookLM Retrieval Assistant for Codex
**Core Value**: Automates Google NotebookLM via local browser automation to retrieve source-constrained answers based on user-uploaded materials, reducing context waste and hallucination risks caused by feeding large documents directly to models.
**Key Features**:
- **Codex Compatibility**: Organized according to Codex skill directory structures, can be directly placed in `~/.codex/skills/notebooklm/` for use.
- **Browser Automation**: Supports logging into Google/NotebookLM via a visible browser and maintains local login sessions.
- **Notebook Management**: Supports locally saving, listing, adding, and querying NotebookLM notebooks.
- **Source-Constrained Q&A**: Asks questions, follow-ups, and synthesizes results strictly around uploaded materials.

**Use Cases**: Knowledge-base Q&A, long-document retrieval augmentation, local Codex workflows requiring NotebookLM source-constrained answers.

### 9. [ADK-Skill-Design-Patterns-zh](./adk-skill-design-patterns-zh/README.md)
**Role**: AI Agent Skill Design Expert
**Core Value**: Provides an in-depth breakdown of the 5 core AI Agent Skill design patterns launched by Google ADK, along with complete Chinese examples and documentation.
**Key Features**:
- **Five Classic Patterns**: Covers Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline patterns.
- **Full Chinese Translation**: The core `SKILL.md` file is deeply localized in Chinese, significantly lowering the barrier to understanding and adoption.
- **Structured Design**: Demonstrates how to build high-quality skills through checklist-driven, template-driven, and workflow-breakdown approaches.
- **Reusable Templates**: Provides standard directory structures and instruction organization methods, serving as scaffolding for new skill development.

**Use Cases**: Systematically learning skill design patterns, rapidly building structured Agent skills, improving stability for complex task processing.

## 🚀 How to Use

### Method 1: Quick Installation (Recommended)
If you have already installed `Skill-Installer`, you can directly use the slash command to install other skills:
```bash
/skill-installer
```

### Method 2: Manually Add Skills and Workflows
1. **Clone the repository**:
   ```bash
   git clone https://github.com/alffei/skill_share.git
   ```

2. **Move contents**:
   Antigravity relies on the `.agent` directory at the project root to identify skills and workflows.
   - **Skills**: Copy folders such as `skill-installer/skills/skill-installer` to the `.agent/skills/` directory.
   - **Workflows**: Copy `.md` files from `skill-installer/workflows/` to the `.agent/workflows/` directory.

3. **Activate and Refresh**:
   - **Skills**: Automatically load based on context when the Agent processes tasks.
   - **Workflows**: For newly added or modified workflows, you need to navigate to Antigravity's **Customizations** page and click the **Refresh** button.

### Method 3: Install to Codex
If you wish to use `NotebookLM-Skill-Codex` in your local Codex, copy or clone the directory to `~/.codex/skills/notebooklm/`:

```bash
git clone https://github.com/alffei/skill_share.git
mkdir -p ~/.codex/skills
cp -R skill_share/notebooklm-skill-codex ~/.codex/skills/notebooklm
```

After installation, the directory structure should resemble:

```text
~/.codex/skills/notebooklm/
├── SKILL.md
├── agents/
├── scripts/
├── references/
└── requirements.txt
```

Before first use, it is recommended to refer to [`notebooklm-skill-codex/README.md`](./notebooklm-skill-codex/README.md) to complete authentication and environment setup.

## ✍️ Contribution Guidelines

1. Create a new folder in the root directory, named after your skill.
2. Create a `SKILL.md` file inside the folder, following the standard Skill definition format.
3. If there are related templates or scripts, place them in the `resources/` or `scripts/` subdirectories within the folder.
4. Submit a Pull Request!

---
Built with [AI神经] for AI Agents.
