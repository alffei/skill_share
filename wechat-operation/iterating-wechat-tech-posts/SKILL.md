---
name: iterating-wechat-tech-posts
description: “Generates endings and CTAs, pre-publish editorial QA, sentence sharpening, and post-performance retrospectives for WeChat tech posts. Use when the user needs a strong ending, final edit pass, paragraph sharpening, analytics review, or iteration plan for tech/engineering WeChat公众号.”
---

# Iterating WeChat Tech Posts

## When to use
结尾三版本、发布前质检、句子变锋利、数据复盘、下一篇怎么改。Use when writing endings, running pre-publish QA, sharpening paragraphs, reviewing post analytics, or planning next iterations.

## Inputs
- 文章主题/正文
- 发布数据（阅读量/完读率/分享/收藏/留言等）可选
- 目标偏好：涨粉/收藏/转发/留言

## Workflow
1. **生成结尾方案** — 输出实用派/观点派/福利派三种结尾
   - ✅ 检查点：每种结尾克制自然，无硬推感
2. **发布前质检** — 检查结构、收益、术语密度、例子贴近度、不确定事实
   - ✅ 检查点：所有不确定事实已列入核实清单
3. **段落锐化** — 逐段改写提升信息密度，输出删除/替换清单
   - ✅ 检查点：改写不改变原意
4. **数据复盘**（若有发布数据）— 原因推断、改进建议、后续3个选题
5. **输出迭代计划** — 综合以上结果，给出下一篇改进方向（参见 TEMPLATES.md）

## Output expectations
- 3种结尾：实用派/观点派/福利派（克制自然）
- 发布前质检：结构、收益、术语密度、例子贴近度、不确定事实清单
- 段落锐化：改写版 + 删除/替换清单
- 数据复盘：原因推断、下次改法、后续3个选题

## Quality checks
- CTA 不要”营业员式硬推”
- 改写不改变原意，但提升信息密度与可读性
- 复盘建议必须具体可执行，不可泛泛而谈

## Examples
User: “这篇文章阅读量2000但完读率只有15%，帮我分析下怎么改”
Assistant: 输出数据复盘（完读率低的3个可能原因）+ 段落锐化建议 + 后续3个选题方向。
