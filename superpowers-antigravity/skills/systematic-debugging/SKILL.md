---
name: systematic-debugging
description: "Systematically diagnoses bugs through structured root cause analysis — reproducing issues, isolating variables, tracing execution paths, and verifying fixes. Use when encountering any bug, test failure, unexpected behavior, build error, or performance regression, especially when previous fix attempts have failed or the root cause is unclear."
---

# Systematic Debugging

## Overview

Finds root cause before attempting fixes. Random fixes waste time and create new bugs.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue: test failures, bugs in production, unexpected behavior, performance problems, build failures, integration issues.

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes or the previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

## The Four Phases

You MUST complete each phase before proceeding to the next. **Checkpoint:** confirm completion of each phase before advancing.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Read stack traces completely — note line numbers, file paths, error codes
   - They often contain the exact solution; don't skip past errors or warnings

2. **Reproduce Consistently**
   - Can you trigger it reliably with exact steps?
   - If not reproducible, gather more data — don't guess

3. **Check Recent Changes**
   - `git diff`, recent commits, new dependencies, config changes, environmental differences

4. **Gather Evidence in Multi-Component Systems**

   **WHEN system has multiple components (CI → build → signing, API → service → database):**

   Add diagnostic instrumentation at each component boundary before proposing fixes:
   ```
   For EACH component boundary:
     - Log what data enters and exits
     - Verify environment/config propagation
     - Check state at each layer
   Run once → analyze evidence → identify failing component → investigate
   ```

   See `defense-in-depth.md` in this directory for multi-layer validation patterns.

5. **Trace Data Flow**

   **WHEN error is deep in call stack:** See `root-cause-tracing.md` in this directory for the complete backward tracing technique.

   **Quick version:** Trace the bad value backward through the call stack — where does it originate? Fix at source, not at symptom.

**Phase 1 checkpoint:** Can you state the root cause in one sentence? If not, keep investigating.

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. **Find Working Examples** — Locate similar working code in the same codebase
2. **Compare Against References** — Read reference implementations COMPLETELY, not skimmed
3. **Identify Differences** — List every difference between working and broken, however small
4. **Understand Dependencies** — Components, settings, config, environment, assumptions

**Phase 2 checkpoint:** Can you list the specific differences between working and broken code?

### Phase 3: Hypothesis and Testing

**Scientific method — one variable at a time:**

1. **Form Single Hypothesis** — State clearly: "I think X is the root cause because Y"
2. **Test Minimally** — Make the SMALLEST possible change. One variable at a time.
3. **Verify** — Did it work? Yes → Phase 4. No → form NEW hypothesis. DON'T stack fixes.
4. **When You Don't Know** — Say so. Ask for help. Research more. Don't pretend.

**Phase 3 checkpoint:** Did your minimal change confirm or disprove the hypothesis?

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. **Create Failing Test Case** — Simplest reproduction. Automated if possible. MUST exist before fixing.
   - **REQUIRED SUB-SKILL:** Use superpowers:test-driven-development for writing proper failing tests
2. **Implement Single Fix** — Address root cause. ONE change. No "while I'm here" improvements.
3. **Verify Fix** — Test passes? No regressions? Issue actually resolved?
4. **If Fix Doesn't Work:**
   - < 3 attempts: Return to Phase 1 with new information
   - **>= 3 attempts: STOP — question the architecture (step 5)**
5. **If 3+ Fixes Failed: Question Architecture**
   - Signs: each fix reveals new coupling, requires "massive refactoring", or creates new symptoms elsewhere
   - **Discuss with your human partner before attempting more fixes** — this is a wrong architecture, not a failed hypothesis

**Phase 4 checkpoint:** Does the fix pass the failing test without regressions?

## Red Flags - STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
- "Here are the main problems: [lists fixes without investigation]"
- Proposing solutions before tracing data flow
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals new problem in different place**

**ALL of these mean: STOP. Return to Phase 1.**

**If 3+ fixes failed:** Question the architecture (see Phase 4.5)

## Human Partner Signals You're Doing It Wrong

**Watch for these redirections — they mean STOP and return to Phase 1:**
- "Is that not happening?" — You assumed without verifying
- "Stop guessing" — Proposing fixes without understanding
- "Ultrathink this" — Question fundamentals, not symptoms
- "We're stuck?" (frustrated) — Your approach isn't working

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question pattern, don't fix again. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare | Identify differences |
| **3. Hypothesis** | Form theory, test minimally | Confirmed or new hypothesis |
| **4. Implementation** | Create test, fix, verify | Bug resolved, tests pass |

## When Process Reveals "No Root Cause"

If systematic investigation reveals the issue is truly environmental, timing-dependent, or external:
1. Document what you investigated
2. Implement appropriate handling (retry, timeout, error message)
3. Add monitoring/logging for future investigation

**But:** 95% of "no root cause" cases are incomplete investigation.

## Supporting Techniques

Available in this directory:
- **`root-cause-tracing.md`** — Trace bugs backward through call stack to find original trigger
- **`defense-in-depth.md`** — Add validation at multiple layers after finding root cause
- **`condition-based-waiting.md`** — Replace arbitrary timeouts with condition polling

**Related skills:**
- **superpowers:test-driven-development** — For creating failing test case (Phase 4, Step 1)
- **superpowers:verification-before-completion** — Verify fix worked before claiming success
