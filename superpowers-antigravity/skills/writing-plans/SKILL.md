---
name: writing-plans
description: "Use when you have a spec, requirements, or design for a multi-step implementation task and need to create a structured plan before touching code. Use when breaking down features into bite-sized TDD tasks with exact file paths, commands, and expected outputs."
---

# Writing Plans

## Overview

Creates comprehensive implementation plans with bite-sized TDD tasks. Assumes the implementing engineer has zero codebase context — documents exact file paths, complete code, test commands, and expected outputs for every step.

**Core principle:** Every step is one action (2-5 minutes). DRY. YAGNI. TDD. Frequent commits.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Context:** Run in a dedicated worktree (created by brainstorming skill).

**Save plans to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Workflow

### Step 1: Gather Requirements

Collect spec, design docs, and acceptance criteria. Identify all components that need to change.

**Checkpoint:** Can you state the goal in one sentence and list every component involved?

### Step 2: Write the Plan Header

Every plan MUST start with:

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]
**Architecture:** [2-3 sentences about approach]
**Tech Stack:** [Key technologies/libraries]
```

### Step 3: Break Down into Tasks

Each task follows this structure — every field is required:

```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test**
[Complete test code — not "add validation"]

**Step 2: Run test to verify it fails**
Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

**Step 3: Write minimal implementation**
[Complete implementation code]

**Step 4: Run test to verify it passes**
Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

**Step 5: Commit**
`git add <files> && git commit -m "feat: add specific feature"`
```

**Checkpoint:** Does each task have exact file paths, complete code, exact commands, and expected output?

### Step 4: Execution Handoff

After saving the plan, offer execution choice:

| Option | Description |
|--------|-------------|
| **Subagent-Driven** (this session) | Dispatch fresh subagent per task, review between tasks. **REQUIRED SUB-SKILL:** superpowers:subagent-driven-development |
| **Parallel Session** (separate) | Open new session in worktree. **REQUIRED SUB-SKILL:** superpowers:executing-plans |

## Rules

- **Exact file paths always** — never "the config file"
- **Complete code in plan** — never "add validation here"
- **Exact commands with expected output** — never "run the tests"
- **Reference relevant skills** with `superpowers:skill-name` syntax
- **One action per step** (2-5 minutes each)
