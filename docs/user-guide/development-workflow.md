# Development Workflow

This guide outlines our recommended development workflow using VS Code and Python.

## Test-Driven Development (TDD)

### 1. Write Test First

Create test file before implementation:

```python
# tests/test_feature.py
def test_new_feature():
    """Test the new feature functionality."""
    result = my_feature()
    assert result == expected_value
```

### 2. Run Test (Red)

Run the test to see it fail:
```bash
pytest tests/test_feature.py -v
```

### 3. Implement Feature (Green)

Write minimal code to pass test:

```python
# src/module.py
def my_feature():
    """Implement the new feature."""
    return expected_value
```

### 4. Refactor

Improve code while keeping tests green:
```python
def my_feature():
    """Implement the new feature with better structure."""
    # Refactored implementation
    return calculate_result()
```

## Code Quality Process

### 1. Auto-Formatting

Black formats code on save:
- Consistent style
- PEP 8 compliance
- Readable diffs

### 2. Linting

Ruff checks for:
- Code style issues
- Potential bugs
- Complexity problems
- Import organization

### 3. Type Checking

Use type hints and mypy:
```python
def process_data(items: list[str]) -> dict[str, int]:
    """Process string items into count dictionary."""
    return {item: items.count(item) for item in set(items)}
```

### 4. Documentation

Write docstrings for all public APIs:
```python
def calculate_metrics(data: pd.DataFrame) -> dict[str, float]:
    """Calculate statistical metrics for DataFrame columns.
    
    Args:
        data: Input DataFrame with numeric columns
        
    Returns:
        Dictionary mapping column names to their metrics
        
    Raises:
        ValueError: If DataFrame has no numeric columns
    """
```

## Git Workflow

### 1. Feature Branch

Create branch for new feature:
```bash
git checkout -b feature/new-feature
```

### 2. Commit Changes

Make small, focused commits:
```bash
git add src/module.py tests/test_module.py
git commit -m "Add new feature with tests"
```

### 3. Keep Updated

Regularly sync with main branch:
```bash
git fetch origin
git rebase origin/main
```

### 4. Code Review

- Push branch
- Create pull request
- Address review comments
- Merge when approved

## Development Cycle

### 1. Planning

1. Understand requirements
2. Design API
3. Write test cases
4. Plan implementation

### 2. Implementation

1. Write failing test
2. Implement feature
3. Run tests
4. Refactor
5. Document

### 3. Review

1. Self-review changes
2. Run all tests
3. Check documentation
4. Create pull request

### 4. Deployment

1. Merge to main
2. Run integration tests
3. Update documentation
4. Deploy changes

## Best Practices

### Code Organization

```
project/
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── test_module1.py
│   └── test_module2.py
└── docs/
    ├── api/
    └── guides/
```

### Testing Strategy

1. Unit Tests
   - Test individual components
   - Mock dependencies
   - Fast execution

2. Integration Tests
   - Test component interaction
   - Minimal mocking
   - Real dependencies

3. End-to-End Tests
   - Test complete workflows
   - Production-like environment
   - Full system integration

### Documentation Types

1. Code Documentation
   - Docstrings
   - Type hints
   - Comments

2. API Documentation
   - Function signatures
   - Parameters
   - Return values
   - Examples

3. User Guides
   - Installation
   - Configuration
   - Usage examples

## Development Environment

### Editor Setup

1. VS Code Extensions
   - Python
   - Pylance
   - Git Lens
   - Test Explorer

2. Workspace Settings
   - Format on save
   - Line length rulers
   - Integrated terminal

3. Keyboard Shortcuts
   - Quick test running
   - Git commands
   - Code navigation

### Tools Integration

1. Testing
   - pytest
   - coverage
   - pytest-cov

2. Code Quality
   - black
   - ruff
   - mypy

3. Documentation
   - mkdocs
   - mkdocstrings

## Continuous Integration

### GitHub Actions

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/
```

### Quality Gates

1. All tests passing
2. Code coverage >= 90%
3. No linting errors
4. Documentation updated

## See Also

- [VS Code Integration](vscode-integration.md)
- [Code Style Guide](../best-practices/code-style.md)
- [Testing Guide](../best-practices/testing.md)
