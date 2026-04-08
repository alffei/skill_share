---
name: requesting-code-review
description: "Dispatches a code-reviewer subagent to evaluate recent changes against requirements — gathering git SHAs, filling the review prompt template, and triaging feedback by severity before proceeding. Use when completing tasks, implementing major features, before merging branches, or when stuck and needing a fresh perspective on code quality."
---

# Requesting Code Review

Dispatches a `superpowers:code-reviewer` subagent to catch issues before they cascade, using a structured prompt template with git SHAs and implementation context.

## When to Use

**Mandatory triggers:**
- After each task in subagent-driven development
- After completing a major feature
- Before merge to main/base branch

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing a complex bug

## Workflow

### 1. Capture Git SHAs
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main for full branch diff
HEAD_SHA=$(git rev-parse HEAD)
```
**Validation:** Both SHAs resolve to valid commits

### 2. Dispatch Code-Reviewer Subagent
Fill the prompt template at `./code-reviewer.md` with these placeholders:

| Placeholder | Value |
|---|---|
| `{WHAT_WAS_IMPLEMENTED}` | What was just built |
| `{PLAN_OR_REQUIREMENTS}` | What it should do (plan file or spec) |
| `{BASE_SHA}` | Starting commit |
| `{HEAD_SHA}` | Ending commit |
| `{DESCRIPTION}` | Brief summary of changes |

Dispatch using the Task tool with `superpowers:code-reviewer` type.

### 3. Triage and Act on Feedback
- **Critical:** Fix immediately — blocks all progress
- **Important:** Fix before proceeding to next task
- **Minor:** Note for later or fix if quick
- **Incorrect feedback:** Push back with technical reasoning and evidence

**Validation:** All Critical and Important issues resolved before continuing

## Example

```
[Completed Task 2: Add verification function]

1. Capture SHAs:
   BASE_SHA=a7981ec  HEAD_SHA=3df7661

2. Dispatch code-reviewer subagent:
   WHAT_WAS_IMPLEMENTED: Verification and repair functions for conversation index
   PLAN_OR_REQUIREMENTS: Task 2 from docs/plans/deployment-plan.md
   BASE_SHA: a7981ec
   HEAD_SHA: 3df7661
   DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types

3. Reviewer returns:
   Strengths: Clean architecture, real tests
   Issues:
     Important: Missing progress indicators
     Minor: Magic number (100) for reporting interval
   Assessment: Ready to proceed after Important fix

4. Fix Important issue (progress indicators) → Continue to Task 3
```

## Integration with Workflows

| Workflow | Review Cadence |
|---|---|
| Subagent-Driven Development | After EACH task |
| Executing Plans | After each batch (3 tasks) |
| Ad-Hoc Development | Before merge or when stuck |

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue with valid technical feedback without evidence

**If reviewer is wrong:**
- Push back with technical reasoning
- Show code/tests that prove correctness
- Request clarification on their concern

See prompt templates at: `./code-reviewer.md` and `./reviewer-prompt.md`
