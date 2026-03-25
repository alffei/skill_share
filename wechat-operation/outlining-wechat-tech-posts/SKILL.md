---
name: outlining-wechat-tech-posts
description: “Builds WeChat-friendly outlines for tech posts including multi-level TOC, reader-benefit lines per section, pitfall checklists, action checklists, and 30-second skim summaries. Use when the user asks for outlines, article structures, tutorial blueprints, or content skeletons for tech/engineering WeChat公众号.”
---

# Outlining WeChat Tech Posts

## When to use
大纲、目录、结构重建、教程型骨架（步骤+检查点+报错）。Use when building outlines, restructuring articles, designing tutorial skeletons, or creating content blueprints.

## Inputs
- 主题
- 内容类型（教程/科普/深度解读/工具评测/复盘/观点）
- 长度目标（默认 1200-2000 字）
- 读者水平（默认中级）

## Workflow
1. **确定内容类型与读者水平** — 明确教程/科普/深度解读等类型
2. **构建3级标题大纲** — 按”先结论后细节”原则搭建结构
   - ✅ 检查点：每节有”读者收益句”
3. **填充落地支撑** — 每节至少包含例子/类比/步骤之一
   - ✅ 检查点：无空洞章节
4. **添加必备模块** — 误区澄清、踩坑清单、行动清单、30秒速读版
5. **教程型额外步骤** — 补充前置条件、检查点、常见失败原因、最终交付物
6. **终审** — 检查结构完整性与长度目标匹配度（参见 TEMPLATES.md 大纲模板）

## Output expectations
- 3级标题大纲
- 每节有”读者收益句”
- 必含：误区澄清、踩坑清单、行动清单、30秒速读版要点
- 教程型：前置条件、步骤1-7、检查点、常见失败原因、最终交付物

## Quality checks
- 先结论后细节
- 每节都有”例子/类比/步骤”至少一个落地支撑
- 大纲层级清晰，不超过3级

## Examples
User: “帮我列一个 Docker 多阶段构建的教程大纲”
Assistant: 输出3级标题大纲（含前置条件、7步骤、检查点、常见失败原因）+ 每节读者收益句 + 30秒速读版。
