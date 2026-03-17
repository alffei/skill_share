---
name: notebooklm
description: Use for querying Google NotebookLM notebooks from Codex via local browser automation. Trigger when the user mentions NotebookLM, shares a NotebookLM URL, wants source-grounded answers from uploaded docs, or needs to add, list, search, activate, or remove notebooks from a local NotebookLM library.
---

# NotebookLM

Use this skill to let Codex query Google NotebookLM and return answers grounded in the user's uploaded documents.

This skill is for local Codex environments that can:
- run shell commands
- install Python dependencies
- access the network
- open a visible browser window for Google login

## Use bundled scripts as black boxes

Always use the wrapper:

```bash
python scripts/run.py <script> [args...]
```

Do not call scripts in `scripts/` directly unless you are debugging the skill itself. The wrapper creates `.venv`, installs dependencies, and runs the script with the correct interpreter.

If the first setup is interrupted, rerun the same wrapper command. The wrapper now repairs incomplete `.venv` directories automatically.

## When to use

Trigger this skill when the user:
- mentions NotebookLM
- shares a NotebookLM URL
- asks to query their docs through NotebookLM
- wants to save or manage NotebookLM notebooks locally
- asks for answers grounded only in uploaded notebook sources

## Core workflow

### 1. Check authentication first

```bash
python scripts/run.py auth_manager.py status
```

If authentication is missing or stale, run setup.

### 2. Authenticate with Google

```bash
python scripts/run.py auth_manager.py setup
```

Important:
- the browser must be visible for login
- tell the user a browser window will open
- wait for them to complete Google login manually

### 3. Resolve the notebook

List saved notebooks:

```bash
python scripts/run.py notebook_manager.py list
```

If the user provided a notebook URL that is not in the library yet, prefer Smart Add:

```bash
python scripts/run.py ask_question.py \
  --question "What is the content of this notebook? What topics are covered? Provide a brief overview." \
  --notebook-url "[URL]"

python scripts/run.py notebook_manager.py add \
  --url "[URL]" \
  --name "[Specific notebook name]" \
  --description "[Specific description based on notebook content]" \
  --topics "[topic1,topic2,topic3]"
```

Do not invent generic metadata if the notebook content is still unknown.

### 4. Ask the notebook

Use one of:

```bash
python scripts/run.py ask_question.py --question "Your question here"
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id
python scripts/run.py ask_question.py --question "..." --notebook-url "https://notebooklm.google.com/notebook/..."
```

Add `--show-browser` only when debugging UI failures.

## Follow-up rule

`ask_question.py` appends a follow-up reminder to every answer. Treat that as an internal prompt to keep researching before answering the user.

Before you respond:
1. Compare the NotebookLM answer to the user's actual request.
2. Identify missing details, edge cases, or implementation gaps.
3. Ask one or more follow-up questions if the first answer is incomplete.
4. Synthesize the final response only after the information is sufficient.

Each NotebookLM query is stateless, so follow-up questions must include the needed context.

## Command reference

Read [commands.md](./references/commands.md) when you need the exact CLI for:
- authentication
- library management
- notebook queries
- cleanup

## Troubleshooting

Read [troubleshooting-codex.md](./references/troubleshooting-codex.md) when:
- login fails
- the browser does not launch
- selectors break after a NotebookLM UI change
- Patchright or Chrome installation fails

## Operational notes

- Skill data is stored under the skill directory in `data/`.
- First use creates `.venv` in the skill directory.
- Environment setup installs Python dependencies and Patchright's Chrome runtime.
- Dependency installation streams pip output so DNS or mirror failures are visible instead of appearing stuck.
- `NOTEBOOKLM_PIP_INDEX_URL` can be used to point pip at a reachable package mirror.
- Authentication uses a persistent browser profile plus saved storage state.
- Free Google accounts may hit NotebookLM rate limits.

## Limits

- Each query opens a fresh browser session.
- The user must already have a NotebookLM notebook with uploaded sources.
- Browser automation may break if NotebookLM changes its UI.
