# Skill Installer for Antigravity

这个目录包含了一个强大的技能安装器 (**Skill Installer**)，用于在 **Antigravity** 环境中方便地管理和安装来自外部仓库（如 GitHub）或官方库的技能。

## 什么是 Skill Installer？
Skill Installer 是一个结构化的工具集，允许 Agent 动态地列出、搜索并安装新的 **Skills**。它可以从指定的 GitHub 仓库或精选的技能列表中拉取代码，并将其部署到全局或当前项目的工作区中。

## 如何在 Antigravity 中使用？

### 1. 安装与设置
Antigravity 支持 **项目级** 和 **全局** 两种安装方式。由于 Skill Installer 是一个通用型工具，建议将其安装在 **全局目录**，以便在所有项目中使用。

- **全局安装（推荐）**：
  - 将 `skills/skill-installer` 移动至 `~/.gemini/antigravity/skills/`
  - 将 `workflows/skill-installer.md` 移动至 `~/.gemini/antigravity/global_workflows/`
- **项目级安装**：
  - 将 `skills/` 和 `workflows/` 文件夹内容移动到项目根目录的 `.agent/` 目录下。
- **刷新配置**：在移动或更新后，前往 Antigravity 的 **Customizations** 页面点击 **Refresh** 按钮。

### 2. 自动技能加载 (Skills)
Antigravity 会自动检索 `.agent/skills/` 目录。当您需要寻找新工具或询问“有哪些可用技能”时，Agent 会加载 `skill-installer` 来辅助您。
- **功能特性**：支持列出精选技能、搜索特定技能以及通过 GitHub URL 直接安装。

### 3. 斜杠命令 (Workflows)
您可以直接在聊天框输入以下命令启动安装流程：
- `/skill-installer`：启动技能安装向导，可以列出可用技能或根据您的输入安装特定技能。

---
*注：安装新技能后，您可能需要重启 Antigravity 以使新技能生效。*
