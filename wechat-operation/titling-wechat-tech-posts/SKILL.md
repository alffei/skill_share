---
name: titling-wechat-tech-posts
description: “Crafts and rewrites WeChat tech post titles across multiple patterns including list, contrast, outcome, scenario, anti-myth, and template styles. Use when the user needs headline brainstorming, title rewrites, clickability optimization, or restrained-but-effective titles for tech/engineering WeChat公众号.”
---

# Titling WeChat Tech Posts

## When to use
需要标题池、标题结构化、标题克制改写、避免标题党但要高点击。Use when brainstorming headlines, rewriting titles, optimizing clickability, or generating title variations across styles.

## Inputs
- 主题
- 读者层级（初级/中级/决策者）
- 风格（爆款风/克制风/学术风）
- 是否允许数字与对比（默认允许但不夸大）

## Workflow
1. **分析主题与读者** — 明确对象/场景/收益三要素
2. **生成标题池** — 按6种结构（清单/对比/结果/场景/反常识/模板）各生成标题
   - ✅ 检查点：共 ≥20个标题，覆盖指定结构
3. **标注元信息** — 每个标题标注适合读者层级 + 点击诱因点
4. **克制改写**（若有原标题）— 输出10个”更克制但更想点”的改写版本
   - ✅ 检查点：无编造数据，无夸大表述
5. **终审** — 逐条检查具体性（对象+场景+收益齐全）（参见 TEMPLATES.md）

## Output expectations
- 20 个标题，覆盖指定结构
- 每个标题标注：适合读者层级 + 点击诱因点
- 10 个”更克制但更想点”的改写版本（若给了原标题）

## Quality checks
- 不编造数据；若没有真实数字，不写”提升30%”，改成”明显/显著/可观”
- 标题必须更具体：对象 + 场景 + 收益
- 避免标题党式夸张，保持技术公信力

## Examples
User: “帮我给这篇 Redis 缓存穿透的文章起20个标题”
Assistant: 输出20个标题（覆盖清单/对比/场景等6种结构），每个标注读者层级与点击诱因。
