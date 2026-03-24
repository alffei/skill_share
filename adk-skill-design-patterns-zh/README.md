# ADK Skill 设计模式示例（中文说明版）

这个目录是 `adk-skill-design-patterns/app/skills` 的中文阅读版，主要用于给中文读者配合文章《Google ADK 分享：5 种常见的 AI Agent Skill 设计模式》一起阅读。

它的目标不是做一套全新实现，而是把 5 个最核心的 `SKILL.md` 示例翻成中文，让读者更容易理解不同 Skill 设计模式各自解决什么问题、该怎么组织结构。

## 这份目录里有什么

目录下包含 5 个示例 Skill，分别对应文章中的 5 种常见模式：

- `app/skills/api-expert/`
  Tool Wrapper 模式。把某个技术栈或工具的约定，封装成按需加载的知识包。
- `app/skills/report-generator/`
  Generator 模式。通过模板和风格规范，稳定产出结构化文档。
- `app/skills/code-reviewer/`
  Reviewer 模式。通过清单驱动的方式，对代码进行结构化审查。
- `app/skills/project-planner/`
  Inversion 模式。先通过结构化提问收集上下文，再生成结果。
- `app/skills/doc-pipeline/`
  Pipeline 模式。把复杂任务拆成带检查点的多阶段流程。

## 中文化范围

目前已完成以下中文化处理：

- 5 个核心 `SKILL.md` 已翻译为中文
- `name`、`metadata`、资源路径等兼容性字段保持不变
- 目录结构保持与原始示例一致，方便对照原文或继续运行

目前仍保留原始示例内容的部分：

- `references/` 中的大部分规范文件
- `assets/` 中的模板文件

这样做的原因很简单：读者主要需要看懂 Skill 的核心设计，而这些辅助文件保留原样，更方便和原始仓库逐项对照。

## 建议怎么读

如果你是第一次接触 Skill 设计，建议按这个顺序看：

1. 先看文章，理解 5 种模式分别解决什么问题
2. 再进入对应目录，只读 `SKILL.md`
3. 最后再根据兴趣查看 `references/` 和 `assets/`，理解它们如何配合 `SKILL.md` 工作

如果你已经有 Agent 开发经验，可以反过来看：

1. 先挑一个最接近你当前任务的模式
2. 看它的 `SKILL.md` 是如何组织指令的
3. 再把自己的规则、模板或清单替换进去

## 一个重要提醒

这些示例更适合当“模式样板”，而不是直接原样拿去上线。

真正落地时，你通常还需要根据自己的团队规范、目标用户、技术栈和输出格式，调整：

- `description` 的触发关键词
- `references/` 里的规则清单
- `assets/` 里的模板结构
- 流程里的检查点和人工确认节点

## 目录结构

```text
adk-skill-design-patterns-zh/
└── skills/
    ├── api-expert/
    ├── report-generator/
    ├── code-reviewer/
    ├── project-planner/
    └── doc-pipeline/
```

如果后续需要，我还可以继续把 `references/` 和 `assets/` 里的辅助文件也补成完整中文版。
