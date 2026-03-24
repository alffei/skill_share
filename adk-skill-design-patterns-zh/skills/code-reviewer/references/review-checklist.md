# Python Code Review Checklist

## Correctness (Severity: error)
- [ ] No undefined variables or missing imports
- [ ] No unreachable code after return/break/continue
- [ ] Exception handling catches specific exceptions, not bare `except:`
- [ ] No mutable default arguments (e.g. `def f(x=[])` is a common bug)
- [ ] Type annotations match actual usage

## Style (Severity: warning)
- [ ] Functions use snake_case, classes use PascalCase
- [ ] Functions are under 30 lines (excluding docstrings)
- [ ] No more than 5 parameters per function
- [ ] No wildcard imports (`from x import *`)
- [ ] Imports grouped: stdlib, third-party, local

## Documentation (Severity: info)
- [ ] Public functions have docstrings
- [ ] Complex logic has inline comments explaining WHY
- [ ] Module has a top-level docstring

## Security (Severity: error)
- [ ] No hardcoded secrets (passwords, API keys, tokens)
- [ ] No dynamic code execution on user-supplied input
- [ ] SQL queries use parameterized statements
- [ ] File paths are validated against path traversal

## Performance (Severity: info)
- [ ] No unnecessary nested loops (O(n^2) when O(n) is possible)
- [ ] Large data processed with generators, not lists
- [ ] No repeated expensive operations inside loops
