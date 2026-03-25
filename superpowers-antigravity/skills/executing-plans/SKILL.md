---
name: executing-plans
description: "Loads a written implementation plan and executes it in batches of three tasks with architect review checkpoints between each batch — reviewing the plan critically, following each step exactly, running verifications, and reporting progress. Use when you have a written implementation plan to execute in a separate session, need batch execution with human review gates, or are continuing work from a brainstorming or planning skill."
---

# Executing Plans

Loads an implementation plan and executes tasks in batches of three, pausing between batches for architect review and feedback before continuing.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

## When to Use

- A written implementation plan exists (from `superpowers:writing-plans` or similar)
- Tasks need human review checkpoints between batches
- Execution happens in a separate session from planning
- For same-session execution with subagents, use `superpowers:subagent-driven-development` instead

## Workflow

### 1. Load and Review Plan
- Read the plan file completely
- Review critically — identify questions, gaps, or concerns
- If concerns exist: raise them with human partner before starting
- If no concerns: create TodoWrite with all tasks and proceed
- **Validation:** Can articulate what each task requires and why

### 2. Execute Batch (Default: 3 Tasks)
For each task in the batch:
1. Mark task as `in_progress`
2. Follow each step exactly as written in the plan
3. Run all verifications specified by the plan
4. Mark task as `completed`
- **Validation:** All verifications pass for every task in the batch

### 3. Report and Wait
Present to human partner:
- What was implemented (per task)
- Verification output (test results, build status)
- Say: "Ready for feedback."
- **Do not proceed** until feedback is received

### 4. Apply Feedback and Continue
- Apply any requested changes from feedback
- Execute the next batch of 3 tasks
- Repeat Steps 2-4 until all tasks are complete

### 5. Complete Development
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED:** Use `superpowers:finishing-a-development-branch`
- Follow that skill to verify tests, present options, execute choice

## Example

```
[Plan: docs/plans/2025-03-20-auth-refactor.md with 7 tasks]

Step 1: Read plan, no concerns, create TodoWrite

Step 2: Execute Batch 1 (Tasks 1-3)
  Task 1: Extract auth middleware → done, tests pass
  Task 2: Add token refresh logic → done, tests pass
  Task 3: Update route guards → done, tests pass

Step 3: Report
  "Batch 1 complete. Extracted middleware, added refresh, updated guards.
   All 12 tests passing. Ready for feedback."

Step 4: Partner says "Looks good, continue"

Step 2: Execute Batch 2 (Tasks 4-6)
  Task 5: Hit blocker — missing OAuth config
  → STOP, ask: "Task 5 needs OAuth client ID. Where is this configured?"

[Partner provides config location, continue]
...

Step 5: All tasks done → use finishing-a-development-branch
```

## When to Stop and Ask

**STOP executing immediately when:**
- Hit a blocker mid-batch (missing dependency, test failure, unclear instruction)
- Plan has critical gaps preventing progress
- An instruction is ambiguous
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## Red Flags

**Never:**
- Skip verifications specified in the plan
- Continue past a batch without reporting and waiting for feedback
- Guess at unclear instructions instead of asking
- Force through blockers

**Always:**
- Review the plan critically before starting
- Follow plan steps exactly as written
- Reference sub-skills when the plan says to
- Stop when blocked
