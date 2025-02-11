# VS Code Integration Guide

This guide covers the key VS Code features and integrations available in our development environment.

## Python Development Features

### IntelliSense

VS Code provides rich Python IntelliSense through Pylance:

- Auto-completion
- Type information
- Function signatures
- Quick documentation
- Import suggestions

To trigger IntelliSense:
- Windows/Linux: `Ctrl+Space`
- macOS: `Cmd+Space`

### Code Navigation

Navigate your codebase efficiently:

- Go to Definition: `F12`
- Peek Definition: `Alt+F12`
- Find All References: `Shift+F12`
- Go to Symbol: `Ctrl+Shift+O`
- Workspace Symbol Search: `Ctrl+T`

### Code Formatting

Automatic code formatting with Black:

- Format on Save (enabled by default)
- Manual formatting: `Shift+Alt+F`
- Format selection: `Ctrl+K Ctrl+F`

Configuration in `.vscode/settings.json`:
```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100]
}
```

### Linting

Real-time code analysis with Ruff:

- Error detection
- Style checking
- Best practice suggestions

Linting settings:
```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true
}
```

## Jupyter Integration

### Interactive Window

The Interactive Python window provides REPL functionality:

1. Open: `Ctrl+Shift+P` → "Python: Create Interactive Window"
2. Run code: Select code and press `Shift+Enter`
3. View variables in Variables window
4. Plot inline visualizations

### Notebook Support

Full Jupyter notebook integration:

- Open `.ipynb` files directly
- Run cells with `Shift+Enter`
- Add/delete cells
- Export to various formats

Features:
- Variable explorer
- Data viewer
- Plot viewer
- Kernel management

### Debugging in Notebooks

Debug Jupyter notebook cells:

1. Enable debugging:
   - Click "Debug Cell" button
   - Use `Ctrl+Shift+D`

2. Set breakpoints:
   - Click gutter
   - Press `F9`

3. Debug controls:
   - Continue: `F5`
   - Step Over: `F10`
   - Step Into: `F11`
   - Step Out: `Shift+F11`

## Git Integration

### Source Control

Built-in Git features:

- View changes: Source Control tab (`Ctrl+Shift+G`)
- Stage changes: Click '+' or `Ctrl+Enter`
- Commit: Enter message and `Ctrl+Enter`
- Push/Pull: Status bar buttons

### Git Lens

Enhanced Git features:

- Line-by-line blame
- File history
- Branch comparison
- Repository visualization

## Debugging

### Launch Configurations

Debug configurations in `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/"],
            "console": "integratedTerminal"
        }
    ]
}
```

### Debug Features

- Set breakpoints: Click gutter or `F9`
- Start debugging: `F5`
- Step Over: `F10`
- Step Into: `F11`
- Step Out: `Shift+F11`
- Continue: `F5`
- Stop: `Shift+F5`

### Debug Console

Interactive debug console:

- Evaluate expressions
- View variable values
- Execute commands

Access: Debug toolbar → Open Debug Console

## Testing

### Test Explorer

Integrated test explorer:

- View all tests
- Run individual tests
- Debug tests
- View test output

Access: Testing sidebar (`Ctrl+Shift+P` → "Test: Focus on Test Explorer View")

### Test Commands

Common test operations:

- Run all tests: `pytest tests/`
- Run specific test: `pytest tests/test_file.py::test_name`
- Generate coverage: `pytest --cov=src tests/`

## Customization

### User Settings

Access settings:
- `Ctrl+,` or
- File → Preferences → Settings

Key settings:
```json
{
    "editor.rulers": [80, 100],
    "editor.renderWhitespace": "all",
    "editor.wordWrap": "on",
    "files.trimTrailingWhitespace": true
}
```

### Keyboard Shortcuts

View/modify shortcuts:
- `Ctrl+K Ctrl+S` or
- File → Preferences → Keyboard Shortcuts

Common customizations:
```json
{
    "key": "ctrl+r",
    "command": "python.execInTerminal"
},
{
    "key": "ctrl+shift+r",
    "command": "python.runCurrentFile"
}
```

## Extensions

### Required Extensions

Core functionality:
- Python
- Pylance
- Jupyter
- Ruff
- Black Formatter

### Recommended Extensions

Additional tools:
- GitLens
- Python Test Explorer
- Python Docstring Generator
- Better Comments
- autoDocstring

## Troubleshooting

### Common Issues

1. Python Interpreter Not Found
   - Command Palette → "Python: Select Interpreter"
   - Choose `.venv` environment

2. Linting Not Working
   - Verify Ruff installation
   - Check settings.json configuration
   - Reload VS Code

3. Debugger Issues
   - Verify launch.json configuration
   - Check Python path
   - Reload window

### Logs and Diagnostics

Access logs:
1. Command Palette → "Developer: Open Logs Folder"
2. Check relevant log files:
   - Python Language Server
   - Jupyter
   - VS Code main log

## See Also

- [Installation Guide](../getting-started/installation.md)
- [Development Workflow](development-workflow.md)
- [Best Practices](../best-practices/code-style.md)
