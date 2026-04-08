---
name: ideating-wechat-tech-topics
description: “Generates WeChat tech article topics, series blueprints, and angles with difficulty and hit-potential scoring. Use when the user asks for topic brainstorming, content calendars, anti-myth angles, series planning, or hit-potential evaluation for tech/engineering WeChat公众号.”
---

# Ideating WeChat Tech Topics

## When to use
选题池、内容月历、系列策划、反常识选题、爆款潜质评估。Use when brainstorming topics, building content calendars, planning article series, or evaluating hit potential for tech accounts.

## Inputs
- 领域 {必填或推断}
- 读者画像 {可选}
- 内容形式偏好（教程/清单/测评/复盘/观点）

## Workflow
1. **按读者任务场景分桶** — 将选题分为上手/避坑/提效/决策四类
   - ✅ 检查点：每个桶至少5个选题
2. **多角度拓展** — 给每桶做”强对比/强清单/强复盘”角度
3. **评分与排序** — 给出收益、难度、潜质评分与原因（透明可复盘）
   - ✅ 检查点：评分维度一致，原因具体可追溯
4. **栏目化规划** — 提炼10个栏目名，每个含3期规划
5. **反常识选题** — 输出10个”误区句→正确句→清单标题”组合
6. **附提示词** — 生成可复制提示词（参见 TEMPLATES.md）

## Output expectations
- 30 个选题（含收益、难度、潜质评分、形式建议）
- 10 个栏目名 + 每个 3 期规划
- 10 个”反常识 + 可落地”选题（含误区句/正确句/清单标题）
- 附可复制提示词（见 TEMPLATES.md）

## Quality checks
- 标题雏形要具体（对象/场景/收益）
- 避免”宏大叙事”，优先”可交付物”
- 每个选题必须有明确的读者收益点

## Examples
User: “我做云原生方向，帮我出30个选题”
Assistant: 按上手/避坑/提效/决策分桶输出30个选题（含评分），10个栏目规划，10个反常识选题。
