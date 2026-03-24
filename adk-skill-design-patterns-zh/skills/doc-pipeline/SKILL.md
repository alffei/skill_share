---
name: doc-pipeline
description: 通过多步骤流水线从 Python 源码生成 API 文档。适用于用户要求为模块编写文档、生成 API 文档或从代码创建说明文档时。
metadata:
  pattern: pipeline
  steps: "4"
---

你正在执行一条文档生成流水线。请按顺序完成每一步。如果某一步失败，不要跳过，也不要继续往下执行。

## 第 1 步 - 解析与盘点

分析用户的 Python 代码，并提取：
- 所有公开类及其方法
- 所有公开函数
- 所有模块级常量
- 已有的 docstring（并标注哪些缺失）

将盘点结果以清单形式展示给用户，并询问：“这就是你想要文档化的完整公共 API 吗？”

## 第 2 步 - 生成 Docstring

对每一个缺少 docstring 的公开函数或方法：
- 加载 `references/docstring-style.md`，获取要求的格式
- 严格按照风格规范生成 docstring
- 将生成的 docstring 展示给用户审批

在用户确认这些 docstring 之前，不要进入第 3 步。

## 第 3 步 - 组装文档

加载 `assets/api-doc-template.md`，作为输出结构。

按照模板，将所有类、函数及其 docstring 汇编成一份 API 参考文档。

文档应包含：
- 带锚点链接的目录
- 每个类或函数各自独立的小节
- 每项对应的参数、返回类型和使用示例

## 第 4 步 - 质量检查

对照 `references/quality-checklist.md` 审查最终文档：
- 每个公开符号都已经写入文档
- 每个参数都有类型和说明
- 每个函数至少包含一个使用示例
- 文中不再残留占位文本

报告质量检查结果。如果发现问题，先修复，再展示最终文档。
