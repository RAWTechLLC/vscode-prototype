# First Steps

This guide walks you through your first development tasks using our VS Code Python environment.

## Opening the Project

1. Launch VS Code:
```bash
code .
```

2. Select Python Interpreter:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose `.venv` environment

3. Verify Environment:
```python
# Open Python Interactive window (Ctrl+Shift+P -> "Python: Create Interactive Window")
import sys
print(sys.executable)  # Should point to .venv
```

## Your First Python Module

### 1. Create a Module

Create `src/calculator.py`:

```python
"""Simple calculator module to demonstrate VS Code features."""

class Calculator:
    """A basic calculator implementation."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference between a and b
        """
        return a - b
```

### 2. Create Tests

Create `tests/test_calculator.py`:

```python
"""Test cases for calculator module."""

import pytest
from src.calculator import Calculator

def test_add():
    """Test addition functionality."""
    calc = Calculator()
    assert calc.add(2, 2) == 4
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract():
    """Test subtraction functionality."""
    calc = Calculator()
    assert calc.subtract(2, 2) == 0
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(0.3, 0.1) == pytest.approx(0.2)
```

### 3. Run Tests

Run tests using VS Code:

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Python: Run All Tests"
3. View results in Test Explorer

Or via terminal:
```bash
pytest tests/ -v
```

## Using the Interactive Window

### 1. Open Interactive Window

- Press `Ctrl+Shift+P`
- Type "Python: Create Interactive Window"
- Select your environment

### 2. Try Some Code

```python
# Import your module
from src.calculator import Calculator

# Create instance
calc = Calculator()

# Try calculations
result = calc.add(10, 20)
print(f"10 + 20 = {result}")

result = calc.subtract(50, 30)
print(f"50 - 30 = {result}")
```

## Debugging Your Code

### 1. Set Breakpoint

1. Open `src/calculator.py`
2. Click in the gutter (left margin) to set a breakpoint
3. Or press `F9` on the line

### 2. Start Debugging

1. Open `tests/test_calculator.py`
2. Press `F5` to start debugging
3. Select "Python: Debug Tests"

### 3. Debug Controls

- Continue (`F5`)
- Step Over (`F10`)
- Step Into (`F11`)
- Step Out (`Shift+F11`)
- Stop (`Shift+F5`)

## Creating Documentation

### 1. Add Docstrings

VS Code helps write docstrings:

1. Type `"""` after function/class definition
2. Press Enter
3. VS Code generates docstring template

Example:
```python
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b
```

### 2. View Documentation

- Hover over function/class names
- Use "Go to Definition" (`F12`)
- View in Interactive Window with `?`

## Using Git

### 1. Initialize Repository

```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. Use Source Control in VS Code

1. Open Source Control tab (`Ctrl+Shift+G`)
2. Stage changes with '+'
3. Enter commit message
4. Click checkmark to commit

## Next Steps

1. Explore [VS Code Features](../user-guide/vscode-integration.md)
2. Review [Development Workflow](../user-guide/development-workflow.md)
3. Learn [Best Practices](../best-practices/code-style.md)

## Tips & Tricks

### Code Navigation

- Go to Definition: `F12`
- Find All References: `Shift+F12`
- Quick Fix: `Ctrl+.`
- Rename Symbol: `F2`

### Productivity

- Command Palette: `Ctrl+Shift+P`
- Quick Open: `Ctrl+P`
- Toggle Terminal: `` Ctrl+` ``
- Toggle Sidebar: `Ctrl+B`

### Code Snippets

1. Type `if` and press Tab
2. Type `def` and press Tab
3. Type `class` and press Tab

### Multi-Cursor Editing

- Add cursor: `Alt+Click`
- Add cursors to all occurrences: `Ctrl+Shift+L`
- Add cursor above/below: `Ctrl+Alt+Up/Down`

## Common Tasks

### Running Code

- Current file: `Ctrl+F5`
- Selection/Line: `Shift+Enter` (in Interactive Window)
- Debug mode: `F5`

### Testing

- Run all tests: Test Explorer
- Run file tests: Right-click in editor
- Debug test: Click debug icon in Test Explorer

### Documentation

- Generate docstring: `"""` + Enter
- View documentation: Hover over symbol
- Search docs: Help viewer

## Troubleshooting

### Common Issues

1. **Module Not Found**
   - Check PYTHONPATH
   - Verify virtual environment
   - Check import statement

2. **Debugger Not Working**
   - Verify launch.json configuration
   - Check Python interpreter
   - Reload VS Code

3. **Tests Not Discovered**
   - Check pytest.ini configuration
   - Verify test file naming
   - Check test function naming

## See Also

- [Configuration Guide](configuration.md)
- [VS Code Integration](../user-guide/vscode-integration.md)
- [Development Workflow](../user-guide/development-workflow.md)
