# Skill Share 🚀

这是一个专门用来分享 **Agent Skill** 的项目，主要包含一些自建自用的技能，旨在提升 AI Agent 在特定场景下的处理效率和标准化程度。

## 📁 目录结构

每个技能都位于独立的文件夹中，包含核心的 `SKILL.md` 指令文件以及相关的模板或资源。

```text
.
├── spec-architect/           # Spec 架构师技能
│   ├── SKILL.md
│   └── resources/
├── ruoyi-code-generator/     # 若依代码生成器技能
│   ├── SKILL.md
│   ├── templates/            # 代码生成模板
│   └── references/           # 参考文档
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

## 🚀 如何使用

1. **克隆仓库**:
   ```bash
   git clone https://github.com/alffei/skill_share.git
   ```

2. **添加技能**:
   将你需要的技能文件夹（如 `spec-architect`）复制到你项目的 `.agent/skills/` 目录下。

3. **激活技能**:
   刷新你的 Agent 或是根据 `SKILL.md` 中的定义激活相应的指令。

## ✍️ 贡献指南

1. 在根目录下创建一个新的文件夹，命名为你的技能名称。
2. 在该文件夹下创建 `SKILL.md`，并遵循标准的 Skill 定义格式。
3. 如果有相关的模板或脚本，请放在文件夹内的 `resources/` 或 `scripts/` 子目录下。
4. 提交 Pull Request！

---
Built with AI 神经 for AI Agents.
