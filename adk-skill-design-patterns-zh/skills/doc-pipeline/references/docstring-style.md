# Docstring Style Guide

Use Google-style docstrings for all public API documentation.

## Function/Method Format

```python
def function_name(param1: str, param2: int = 0) -> bool:
    """One-line summary of what the function does.

    Extended description if the one-liner isn't enough.
    Explain the behavior, not the implementation.

    Args:
        param1: Description of param1. Include valid values if constrained.
        param2: Description of param2. Mention the default behavior.

    Returns:
        Description of the return value. Include possible values.

    Raises:
        ValueError: When param1 is empty.
        TypeError: When param2 is not an integer.

    Example:
        >>> result = function_name("hello", 42)
        >>> print(result)
        True
    """
```

## Class Format

```python
class ClassName:
    """One-line summary of the class.

    Extended description of the class purpose and behavior.

    Attributes:
        attr1: Description of attr1.
        attr2: Description of attr2.

    Example:
        >>> obj = ClassName(attr1="value")
        >>> obj.method()
    """
```

## Rules
- First line is always a one-line imperative summary ("Return X", "Calculate Y")
- Leave a blank line between the summary and extended description
- Document ALL parameters, return values, and raised exceptions
- Include at least one usage example with expected output
