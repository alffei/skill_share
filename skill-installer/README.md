# Skill Installer for Antigravity 🛠️
 
这个目录包含了一个强大的技能安装器 (**Skill Installer**)，用于在 **Antigravity** 环境中方便地管理和安装来自外部仓库（如 GitHub）或官方库的技能。

## 📖 简介

Skill Installer 是一个结构化的工具集，允许 Agent 动态地列出、搜索并安装新的 **Skills**。它可以从指定的 GitHub 仓库或精选的技能列表中拉取代码，并将其部署到全局或当前项目的工作区中。

## 🚀 安装与设置

Antigravity 支持 **项目级** 和 **全局** 两种安装方式。由于 Skill Installer 是一个通用型工具，建议将其安装在 **全局目录**，以便在所有项目中使用。

### 1. 移动文件

- **全局安装（推荐）**:
  - 将 `skills/skill-installer` 文件夹移动至 `~/.gemini/antigravity/skills/`
  - 将 `workflows/skill-installer.md` 文件移动至 `~/.gemini/antigravity/global_workflows/`
- **项目级安装**:
  - 将 `skills/` 和 `workflows/` 文件夹内容复制到项目根目录的 `.agent/` 目录下。

### 2. 刷新配置
在移动或更新后，前往 Antigravity 的 **Customizations** 页面点击 **Refresh** 按钮，使新技能和工作流生效。

## 💡 使用方法

### 自动技能加载 (Skills)
Antigravity 会根据您的询问自动加载 `skill-installer`。例如，您可以问：
- "有哪些可用的技能可以安装？"
- "帮我从 GitHub 安装一个技能"

### 斜杠命令 (Workflows)
您也可以直接在聊天框输入命令启动：
- `/skill-installer`：启动技能安装向导，按提示操作即可。

---
> **注意**: 安装新技能后，您可能需要重启 Antigravity 以使新技能生效。
