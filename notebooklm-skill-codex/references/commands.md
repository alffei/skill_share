# Commands

Always run scripts through the wrapper:

```bash
python scripts/run.py <script> [args...]
```

## Authentication

Check status:

```bash
python scripts/run.py auth_manager.py status
```

Set up login with a visible browser:

```bash
python scripts/run.py auth_manager.py setup
```

Re-authenticate:

```bash
python scripts/run.py auth_manager.py reauth
```

Validate saved auth:

```bash
python scripts/run.py auth_manager.py validate
```

Clear auth:

```bash
python scripts/run.py auth_manager.py clear
```

## Notebook library

List:

```bash
python scripts/run.py notebook_manager.py list
```

Add:

```bash
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Notebook Name" \
  --description "What the notebook contains" \
  --topics "topic1,topic2,topic3"
```

Search:

```bash
python scripts/run.py notebook_manager.py search --query "keyword"
```

Activate:

```bash
python scripts/run.py notebook_manager.py activate --id notebook-id
```

Remove:

```bash
python scripts/run.py notebook_manager.py remove --id notebook-id
```

Stats:

```bash
python scripts/run.py notebook_manager.py stats
```

## Notebook queries

Use active notebook:

```bash
python scripts/run.py ask_question.py --question "Your question here"
```

Use a specific saved notebook:

```bash
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id
```

Use a direct NotebookLM URL:

```bash
python scripts/run.py ask_question.py --question "..." --notebook-url "https://notebooklm.google.com/notebook/..."
```

Show browser during query debugging:

```bash
python scripts/run.py ask_question.py --question "..." --show-browser
```

## Cleanup

Preview cleanup:

```bash
python scripts/run.py cleanup_manager.py
```

Execute cleanup:

```bash
python scripts/run.py cleanup_manager.py --confirm
```

Preserve saved notebook library:

```bash
python scripts/run.py cleanup_manager.py --confirm --preserve-library
```
