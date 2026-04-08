---
name: writing-wechat-tech-posts
description: “Writes complete publish-ready WeChat tech posts including hooks, TOC, body, checklists, image placement, layout notes, and summaries. Use when the user asks to draft a WeChat tech article, generate reusable writing prompts, popularize complex concepts, or turn a topic or outline into a publish-ready post.”
---

# Writing WeChat Tech Posts

## When to use
一键成稿、开头钩子、分节写作、复杂概念科普化、教程/深度文输出、提示词库生成。Use when drafting full articles, writing hooks, popularizing complex concepts, generating writing prompts, or converting outlines to publish-ready posts.

## Inputs
- 账号定位/读者画像（缺省可用”工程/产品/研发从业者”）
- 主题
- 内容类型
- 目标（学会/理解/能上手/能决策/能避坑）
- 合规：不编造数据、不确定要标注”需核实+核实路径”

## Workflow
1. **收口需求** — 用”总控模板”确认主题、类型、读者、目标（参见 TEMPLATES.md）
   - ✅ 检查点：所有输入字段已确认或标记默认值
2. **撰写开头钩子** — 用”5种开头法”生成100-150字钩子
   - ✅ 检查点：钩子有明确的读者痛点或好奇心触发
3. **构建文章结构** — 3级标题目录 + 每节”核心观点→解释→例子/类比→步骤/清单”
4. **正文写作** — 逐节撰写，术语密集处用”类比→定义→流程→误解→MVP”模式
   - ✅ 检查点：类比后必须有严谨定义，不确定事实已标注
5. **补充清单与配图** — 至少1个踩坑清单 + 1个行动清单 + 配图建议
6. **排版与结尾** — 加粗点/金句/分隔线/emoji克制 + 总结/互动/关注引导
7. **生成摘要** — 30字摘要 + 80字摘要
   - ✅ 检查点：全文符合9项输出要求

## Output expectations (publish-ready)
必须包含：
1) 3-5个备选标题（爆款风/克制风/学术风）
2) 开头钩子（100-150字）
3) 文章目录（3级标题）
4) 正文：每节”核心观点→解释→例子/类比→步骤/清单”
5) 至少1个踩坑清单 + 1个行动清单
6) 配图建议（画什么/放哪段后）
7) 排版建议（加粗点/金句/分隔线/emoji克制）
8) 结尾：总结+互动提问+关注引导（自然克制）
9) 30字摘要 + 80字摘要

## Quality checks
- 技术不降智：类比后必须给严谨定义
- 每屏信息密度适中：段落短、清单多
- 不确定事实必须显式标注与核实路径
- 全文长度与内容类型匹配（教程型偏长，观点型偏短）

## Examples
User: “帮我写一篇关于 gRPC vs REST 的科普文章”
Assistant: 输出完整发布稿：5个备选标题、开头钩子、3级目录、正文（含类比与严谨定义）、踩坑清单、行动清单、配图建议、排版建议、结尾、30字+80字摘要。
