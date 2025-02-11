# VS Code Integration

This guide covers the VS Code features and integrations available in the prototype environment.

## Python Development Features

### IntelliSense

VS Code provides rich Python IntelliSense through Pylance:

- Auto-completion
- Type checking
- Import suggestions
- Function signatures
- Quick documentation

### Code Navigation

Navigate your codebase efficiently:

- Go to Definition (F12)
- Find All References (Shift+F12)
- Go to Symbol (Ctrl+T)
- Breadcrumbs navigation
- Outline view

### Debugging

Advanced debugging capabilities:

1. Breakpoints:
   - Line breakpoints (F9)
   - Conditional breakpoints
   - Logpoints
   - Data breakpoints

2. Debug Actions:
   - Start/Continue (F5)
   - Step Over (F10)
   - Step Into (F11)
   - Step Out (Shift+F11)
   - Restart (Ctrl+Shift+F5)

3. Debug Views:
   - Variables
   - Watch
   - Call Stack
   - Breakpoints

## Jupyter Integration

### Interactive Development

1. Jupyter Notebooks:
   - Create new notebooks
   - Import existing notebooks
   - Export to various formats

2. Interactive Window:
   - Run code cells (#%%)
   - View plots inline
   - Variable explorer
   - Data viewer

### Cell Operations

```python
#%% [markdown]
# This is a markdown cell

#%%
# This is a code cell
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3]})
df.head()
```

## Git Integration

### Source Control

Built-in Git features:

- Stage changes
- Commit
- Push/Pull
- Branch management
- Merge conflict resolution

### GitHub Integration

With GitHub Pull Requests extension:

- Review PRs
- Comment on code
- Suggest changes
- Merge PRs

## Terminal Integration

### Integrated Terminal

- Multiple terminals
- Split terminals
- Custom shell configurations
- Task running

### Task Runner

Configure tasks in `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "pytest",
      "group": {
        "kind": "test",
        "isDefault": true
      }
    }
  ]
}
```

## Extensions

### Required Extensions

1. Python:
   - Python extension
   - Pylance
   - Python Test Explorer

2. Documentation:
   - reStructuredText
   - Markdown All in One

3. Git:
   - GitLens
   - GitHub Pull Requests

### Recommended Extensions

1. Productivity:
   - Path Intellisense
   - Todo Tree
   - Better Comments

2. Code Quality:
   - Error Lens
   - Code Spell Checker

3. Themes:
   - Material Icon Theme
   - Atom One Dark Theme

## Workspace Settings

### Python Settings

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.analysis.typeCheckingMode": "basic",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true
}
```

### Editor Settings

```json
{
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "editor.renderWhitespace": "all",
  "editor.suggestSelection": "first",
  "files.trimTrailingWhitespace": true
}
```

## Customization

### Keyboard Shortcuts

Common shortcuts:

- Command Palette: Ctrl+Shift+P
- Quick Open: Ctrl+P
- Toggle Terminal: Ctrl+`
- Toggle Sidebar: Ctrl+B
- Format Document: Alt+Shift+F

### Custom Keybindings

Add custom keybindings in `keybindings.json`:

```json
[
  {
    "key": "ctrl+k ctrl+t",
    "command": "python.runtests"
  }
]
```

## Troubleshooting

### Common Issues

1. Python Interpreter:
   - Command Palette > "Python: Select Interpreter"
   - Choose `.venv` environment

2. Extension Issues:
   - Reload Window
   - Reinstall extension
   - Clear extension cache

3. IntelliSense:
   - Reload Language Server
   - Rebuild IntelliSense database

### Logs and Diagnostics

Access logs:
- Command Palette > "Developer: Open Logs Folder"
- Help > Toggle Developer Tools

## Next Steps

- Explore [Extensions](extensions.md) in detail
- Review [Development Workflow](development-workflow.md)
- Check [Best Practices](../best-practices/code-style.md)
