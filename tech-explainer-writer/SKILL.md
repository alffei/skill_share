---
name: tech-explainer-writer
description: Use when drafting, rewriting, or polishing public-facing tech explainers for general readers. Trigger on requests to explain complex technical concepts, AI products, system mechanisms, industry trends, or jargon-heavy material in plain language; to turn notes, links, transcripts, slides, or drafts into popular-science articles,公众号内容, scripts, summaries, or “一看就懂” explanations.
---

# Tech Explainer Writer

## Overview

Write like a top-tier technology explainer for non-specialists. Make difficult topics easy to understand without flattening away the real mechanism, significance, or tradeoffs.

Prioritize comprehension over terminology. Default audience: general readers, tech-curious readers, and non-specialists.

## Core Workflow

### 1. Identify the knowledge gap

Decide what the reader does not yet understand:

- What is it
- How it works
- Why it matters
- What changes in practice
- Where people usually misunderstand it

State the answer in one plain sentence before expanding.

### 2. Build a reader-first structure

Default structure:

1. Hook with the practical question
2. Explain the core concept in plain words
3. Break down the mechanism step by step
4. Add one concrete example, analogy, or scene
5. Explain meaning, impact, or tradeoffs
6. End with a short takeaway

Use shorter sections when the user asks for concise copy. Compress aggressively before dropping key meaning.

### 3. Explain in layers

Prefer this sequence:

- Concept: define it in plain language
- Mechanism: explain what makes it work
- Example: show what it looks like in real use
- Meaning: explain why readers should care

If the topic is abstract, use one grounded analogy. Stop at one or two analogies; too many dilute precision.

### 4. Keep the language sharp

- Prefer short sentences.
- Explain one point per paragraph.
- Translate jargon on first use.
- Keep the real technical noun when it matters, then explain it.
- Cut filler, scene-setting, and repeated claims.

Good:

> Transformer can be understood as a way for AI to judge which words matter most to each other.

Weak:

> Transformer is a revolutionary architecture that significantly improves contextual understanding.

### 5. Preserve rigor

- Do not oversimplify into something false.
- Flag uncertainty instead of bluffing.
- Separate fact, inference, and analogy.
- When current facts may have changed, verify them before writing.

## Output Pattern

Default to this shape unless the user asks otherwise:

1. Title
2. One-sentence answer
3. Main explanation with short subheads
4. Example or analogy
5. Why it matters
6. Short conclusion

Also provide, when useful:

- 3 alternate titles
- a 60-100 word summary
- a short social caption
- a bullet list version for quick reading

## Rewrite Rules

When rewriting existing drafts:

- Keep the original factual claims unless they are wrong or unsupported
- Remove repeated setup and repeated conclusions
- Move conclusions forward
- Replace stacked abstractions with concrete verbs
- Split long paragraphs
- Turn dense terminology into “term + plain explanation”

If the user asks for “简洁”“一看就懂”“不要长篇大论”, compress first at the sentence level, then at the section level.

## Common Mistakes

- Explaining terms with more terms
- Using three analogies where one would do
- Writing in a lecture tone instead of a reader tone
- Chasing elegance and losing clarity
- Cutting so hard that the causal chain disappears

## References

- Read [style-patterns.md](./references/style-patterns.md) when choosing structure, analogies, and compression tactics.
