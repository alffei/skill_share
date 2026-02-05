# Skill Share 🚀

这是一个专门用来分享 **Agent Skill** 的项目，主要包含一些自建自用的技能，旨在提升 AI Agent 在特定场景下的处理效率和标准化程度。

## 📁 目录结构

每个技能都位于独立的文件夹中，包含核心的 `SKILL.md` 指令文件以及相关的模板或资源。

```text
.
├── spec-architect/           # Spec 架构师技能
├── ruoyi-code-generator/      # 若依代码生成器技能
├── springboot-init/          # Spring Boot 初始化技能
├── wechat-operation/         # 公众号运营技能
├── superpowers-antigravity/  # Antigravity 核心能力集 (移植自 Superpowers)
├── skill-installer/           # 技能安装器 (一键安装/更新技能)
└── README.md
```

## 🛠 已包含的技能

### 1. [Spec-Architect](./spec-architect/SKILL.md)
**角色**: 专业系统架构师
**核心价值**: 拒绝 "Vibe Coding"（随性编码），通过严格的 Spec 流程确保代码实现的准确性。
**工作流**:
1. **Phase 1: Requirements (需求定义)** - 将模糊想法转化为结构化的需求文档。
2. **Phase 2: Design (架构设计)** - 基于需求生成架构图、数据模型和接口设计。
3. **Phase 3: Planning (任务拆解)** - 将设计拆解为可执行的原子化任务。

### 2. [RuoYi-Code-Generator](./ruoyi-code-generator/SKILL.md)
**角色**: 若依框架代码生成器
**核心价值**: 基于数据表结构自动生成符合若依框架规范的完整 CRUD 代码，大幅提升开发效率。
**生成内容**:
- **Java 后端**: Domain、Mapper、Service、ServiceImpl、Controller
- **MyBatis**: XML 映射文件
- **Vue 前端**: API 封装、列表页面组件
- **SQL 脚本**: 菜单初始化 SQL

**适用场景**: 创建新模块、添加业务功能、根据表结构快速生成标准代码。

### 3. [SpringBoot-Init](./springboot-init/SKILL.md)
**角色**: 专业 Spring 开发架构师
**核心价值**: 快速初始化高标准的 Spring Boot 项目骨架，集成最佳实践，避免重复搭建基础架构。
**关键特性**:
- **快速初始化**: 包含 `pom.xml`、`application.yml` 及核心基础类。
- **强制规范**: 严格定义数据流向 (DTO/VO/Entity) 与事务管理。
- **现代化**: 深度集成 JDK 17+ Record 与 MyBatis-Plus。
- **自动工作流**: 提供项目初始化与业务模块新增的标准化操作流。

**适用场景**: 新项目启航、基础架构统一、单体应用标准化。

### 4. [WeChat-Operation](./wechat-operation/README.md)
**角色**: 公众号运营专家
**核心价值**: 覆盖从账号定位、选题策划到爆款创作的全流程，提升技术号运营效率。
**关键特性**:
- **全流程覆盖**: 包含定位、选题、标题、大纲、写作、案例、排版、迭代 8 个子技能。
- **标准化模板**: 每个子技能均配套成熟的 Prompt 模板。
- **技术特色**: 针对科技/工程类公众号优化，拒绝低质内容。

**适用场景**: 公众号冷启动、技术文章创作、运营流程标准化。

### 5. [Superpowers-Antigravity](./superpowers-antigravity/README.md)
**角色**: 资深软件工程师 / 架构师
**核心价值**: 移植自著名的 [Superpowers](https://github.com/obra/superpowers)，这是一套结构化的软件开发工作流，通过强制 Agent 遵循最佳工程实践，大幅提升开发成功率。
**关键特性**:
- **系统化调试**: 包含根因追踪、防御性编程等高级调试技能。
- **标准化工作流**: 提供需求头脑风暴、任务拆解、批量执行等斜杠命令。
- **质量保障**: 集成测试驱动开发 (TDD) 和严格的完成前验证流程。

**适用场景**: 复杂业务开发、系统重构、深度 Bug 修复。

### 6. [Skill-Installer](./skill-installer/README.md)
**角色**: 技能管理专家
**核心价值**: 简化技能的发现与安装过程，支持从 GitHub 仓库或精选列表一键部署技能到 Antigravity。
**关键特性**:
- **多源支持**: 支持 GitHub 仓库 URL 或仓库路径安装。
- **灵活部署**: 支持安装到全局目录或当前项目工作区。
- **自动搜索**: 支持列出推荐的官方/社区技能。

**适用场景**: 环境初始化、快速安装新工具、跨项目同步技能。

## 🚀 如何使用

### 方式一：快速安装 (推荐)
如果您已经安装了 `Skill-Installer`，可以直接使用斜杠命令安装其他技能：
```bash
/skill-installer
```

### 方式二：手动添加技能与工作流
1. **克隆仓库**:
   ```bash
   git clone https://github.com/alffei/skill_share.git
   ```

2. **移动内容**:
   Antigravity 依赖项目根目录下的 `.agent` 目录来识别技能和工作流。
   - **Skills**: 将 `skill-installer/skills/skill-installer` 等文件夹复制到 `.agent/skills/` 目录下。
   - **Workflows**: 将 `skill-installer/workflows/` 中的 `.md` 文件复制到 `.agent/workflows/` 目录下。

3. **激活与刷新**:
   - **Skills**: 会在 Agent 处理任务时根据上下文自动加载。
   - **Workflows**: 对于新增或修改的工作流，您需要前往 Antigravity 的 **Customizations** 页面点击 **Refresh** 按钮。

## ✍️ 贡献指南

1. 在根目录下创建一个新的文件夹，命名为你的技能名称。
2. 在该文件夹下创建 `SKILL.md`，并遵循标准的 Skill 定义格式。
3. 如果有相关的模板或脚本，请放在文件夹内的 `resources/` 或 `scripts/` 子目录下。
4. 提交 Pull Request！

---
Built with [AI神经] for AI Agents.
