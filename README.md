# Skill Share 🚀

这是一个专门用来分享 **Agent Skill** 的项目，主要包含一些自建自用的技能，旨在提升 AI Agent 在特定场景下的处理效率和标准化程度。

## 📁 目录结构

每个技能都位于独立的文件夹中，包含核心的 `SKILL.md` 指令文件以及相关的模板或资源。

```text
.
├── spec-architect/        # 技能文件夹
│   ├── SKILL.md           # 技能指令定义
│   └── resources/         # 技能依赖的模板或资源
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
Built with ❤️ for AI Agents.
