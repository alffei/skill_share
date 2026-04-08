---
name: brainstorming
description: "Turns ideas into fully formed designs and specs through collaborative dialogue — asking one question at a time to refine intent, proposing multiple approaches with trade-offs, and presenting the design incrementally for validation. Use when starting any creative work such as creating features, building components, adding functionality, or modifying behavior before implementation begins."
---

# Brainstorming Ideas Into Designs

Turns ideas into fully formed designs through collaborative dialogue: understand context, refine intent with targeted questions, explore approaches, and present the design incrementally for validation.

## When to Use

- Starting a new feature, component, or significant behavior change
- Exploring an idea before committing to implementation
- Translating vague requirements into a concrete, actionable design
- Before using `superpowers:writing-plans` to create an implementation plan

## Workflow

### 1. Understand the Project Context
- Read relevant files, docs, and recent commits
- Identify existing patterns, constraints, and conventions
- **Validation:** Confirm you can describe the current state of the area being changed

### 2. Refine the Idea Through Questions
- Ask **one question per message** — never batch multiple questions
- Prefer **multiple choice** questions when possible (easier to answer)
- Focus on: purpose, constraints, success criteria, edge cases
- Continue until you can articulate what is being built and why

### 3. Explore Approaches
- Propose **2-3 approaches** with clear trade-offs
- Lead with your recommended option and explain why
- Wait for confirmation before proceeding to design

### 4. Present the Design Incrementally
- Break the design into sections of **200-300 words**
- After each section, ask: "Does this look right so far?"
- Cover: architecture, components, data flow, error handling, testing
- Revise any section based on feedback before continuing

### 5. Document the Design
- Write the validated design to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- Use `elements-of-style:writing-clearly-and-concisely` skill if available
- Commit the design document to git

### 6. Transition to Implementation (Optional)
- Ask: "Ready to set up for implementation?"
- Use `superpowers:using-git-worktrees` to create an isolated workspace
- Use `superpowers:writing-plans` to create a detailed implementation plan

## Example

```
User: "I want to add notifications to the app"

[Step 1: Read existing code, find no notification system exists]

You: "What kind of events should trigger a notification?
  A) User actions (comments, mentions, assignments)
  B) System events (deploys, failures, thresholds)
  C) Both"

User: "A — just user actions for now"

You: "Should notifications be real-time (WebSocket) or polled?
  A) Real-time push
  B) Poll every N seconds
  C) Start with polling, migrate to real-time later"

User: "C"

[Step 3: Present 2 approaches — event bus vs direct insertion]
[Step 4: Present design in sections, validate each]
[Step 5: Write to docs/plans/2025-03-25-notifications-design.md]
```

## Key Principles

- **One question at a time** — do not overwhelm with multiple questions
- **Multiple choice preferred** — easier to answer than open-ended
- **YAGNI ruthlessly** — remove unnecessary features from all designs
- **Explore alternatives** — always propose 2-3 approaches before settling
- **Incremental validation** — present design in sections, validate each
- **Be flexible** — go back and clarify when something does not make sense
