---
name: evidencing-wechat-tech-posts
description: “Produces credible case-study writeups, non-hallucinated data handling, and fact-check lists for WeChat tech posts. Use when the user needs a project recap, results narrative, citations guidance, data verification, or 'what to verify' checklists in tech/engineering WeChat公众号.”
---

# Evidencing WeChat Tech Posts

## When to use
案例复盘写作、数据引用合规、事实核查清单、避免”张口就来”。Use when drafting case studies, verifying data citations, building fact-check checklists, or writing project retrospectives.

## Inputs
- 案例要素：背景/目标/约束/方案/结果/教训（缺省可用 {待补充}）
- 是否允许使用外部来源（若无来源则只给核实路径）

## Workflow
1. **收集案例要素** — 确认背景/目标/约束/方案/结果/教训六要素齐全，缺失项标记 `{待补充}`
2. **构建复盘结构** — 按”问题→选择→取舍→验证→结果→反思”组织叙事
   - ✅ 检查点：每个环节有具体数据或事实支撑，无空泛描述
3. **生成事实核查清单** — 列出所有需核实点、核实方法、核实状态
   - ✅ 检查点：清单 ≥8 条，每条含核实路径
4. **生成可复用模板** — 输出读者可直接套用的复盘/核查模板（参见 TEMPLATES.md）
5. **终审质量关** — 逐条检查质量标准，确认无夸大表述

## Output expectations
- 复盘结构：问题→选择→取舍→验证→结果→反思
- 读者可复用模板/检查清单（≥8条）
- “事实核查清单”：列出所有需要核实点 + 核实方法

## Quality checks
- 不夸大：禁用”颠覆/史诗级”这类词
- 结果表述要带边界：条件/口径/数据来源
- 所有数据引用必须标注来源或标记”需核实”

## Examples
User: “帮我写一个从 MySQL 迁移到 TiDB 的案例复盘”
Assistant: 按复盘六要素收集信息，输出完整复盘文章 + 8条事实核查清单 + 可复用迁移决策模板。
