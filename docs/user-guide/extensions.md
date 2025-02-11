# VS Code Extensions Guide

This guide covers the recommended VS Code extensions and their configurations for Python development.

## Core Extensions

### Python Development

1. **Python** (ms-python.python)
   - IntelliSense
   - Linting
   - Debugging
   - Testing
   - Jupyter support
   
   Configuration:
   ```json
   {
       "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
       "python.analysis.typeCheckingMode": "basic",
       "python.analysis.autoImportCompletions": true
   }
   ```

2. **Pylance** (ms-python.vscode-pylance)
   - Fast type checking
   - Import organization
   - Type inference
   
   Configuration:
   ```json
   {
       "python.analysis.diagnosticMode": "workspace",
       "python.analysis.indexing": true,
       "python.analysis.autoSearchPaths": true
   }
   ```

### Code Quality

1. **Black Formatter** (ms-python.black-formatter)
   - Automatic code formatting
   - PEP 8 compliance
   
   Configuration:
   ```json
   {
       "python.formatting.provider": "black",
       "editor.formatOnSave": true,
       "editor.formatOnPaste": false
   }
   ```

2. **Ruff** (charliermarsh.ruff)
   - Fast Python linting
   - Code style checking
   
   Configuration:
   ```json
   {
       "python.linting.enabled": true,
       "python.linting.flake8Enabled": false,
       "python.linting.ruffEnabled": true
   }
   ```

## Testing Extensions

### Test Management

1. **Python Test Explorer** (littlefoxteam.vscode-python-test-adapter)
   - Visual test runner
   - Test discovery
   - Test debugging
   
   Configuration:
   ```json
   {
       "pythonTestExplorer.testFramework": "pytest",
       "pythonTestExplorer.autoDiscover": "true"
   }
   ```

2. **Coverage Gutters** (ryanluker.vscode-coverage-gutters)
   - Coverage visualization
   - Line highlighting
   
   Configuration:
   ```json
   {
       "coverage-gutters.showLineCoverage": true,
       "coverage-gutters.showRulerCoverage": true
   }
   ```

## Documentation Extensions

### Documentation Tools

1. **Python Docstring Generator** (njpwerner.autodocstring)
   - Automatic docstring generation
   - Multiple docstring formats
   
   Configuration:
   ```json
   {
       "autoDocstring.docstringFormat": "google",
       "autoDocstring.startOnNewLine": true,
       "autoDocstring.includeDescription": true
   }
   ```

2. **Markdown All in One** (yzhang.markdown-all-in-one)
   - Markdown shortcuts
   - Table of contents
   - Preview
   
   Configuration:
   ```json
   {
       "markdown.extension.toc.updateOnSave": true,
       "markdown.extension.preview.autoShowPreviewToSide": false
   }
   ```

## Git Integration

### Version Control

1. **GitLens** (eamodio.gitlens)
   - Git blame annotations
   - File history
   - Repository visualization
   
   Configuration:
   ```json
   {
       "gitlens.codeLens.enabled": true,
       "gitlens.currentLine.enabled": true,
       "gitlens.hovers.currentLine.over": "line"
   }
   ```

2. **Git Graph** (mhutchie.git-graph)
   - Repository visualization
   - Branch management
   
   Configuration:
   ```json
   {
       "git-graph.repository.commits.showSignatureStatus": true,
       "git-graph.date.format": "ISO"
   }
   ```

## Productivity Extensions

### Development Tools

1. **Visual Studio IntelliCode** (visualstudioexptteam.vscodeintellicode)
   - AI-assisted development
   - Smart completions
   
   Configuration:
   ```json
   {
       "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue"
   }
   ```

2. **Better Comments** (aaron-bond.better-comments)
   - Comment highlighting
   - TODO tracking
   
   Configuration:
   ```json
   {
       "better-comments.tags": [
           {
               "tag": "!",
               "color": "#FF2D00",
               "strikethrough": false,
               "backgroundColor": "transparent"
           },
           {
               "tag": "?",
               "color": "#3498DB",
               "strikethrough": false,
               "backgroundColor": "transparent"
           },
           {
               "tag": "//",
               "color": "#474747",
               "strikethrough": true,
               "backgroundColor": "transparent"
           },
           {
               "tag": "todo",
               "color": "#FF8C00",
               "strikethrough": false,
               "backgroundColor": "transparent"
           },
           {
               "tag": "*",
               "color": "#98C379",
               "strikethrough": false,
               "backgroundColor": "transparent"
           }
       ]
   }
   ```

## Extension Pack

### Recommended Extensions List

Create `.vscode/extensions.json`:
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "charliermarsh.ruff",
        "littlefoxteam.vscode-python-test-adapter",
        "ryanluker.vscode-coverage-gutters",
        "njpwerner.autodocstring",
        "yzhang.markdown-all-in-one",
        "eamodio.gitlens",
        "mhutchie.git-graph",
        "visualstudioexptteam.vscodeintellicode",
        "aaron-bond.better-comments"
    ]
}
```

## Installation

### Bulk Installation

Install all recommended extensions:

1. Open VS Code
2. Go to Extensions view (Ctrl+Shift+X)
3. Type `@recommended` in search box
4. Click "Install Workspace Recommended Extensions"

### Manual Installation

Install individual extensions:

1. Open VS Code Quick Open (Ctrl+P)
2. Run command:
   ```
   ext install extension-id
   ```

## Configuration

### Settings Sync

Enable Settings Sync:

1. Open Command Palette (Ctrl+Shift+P)
2. Type "Settings Sync"
3. Choose "Settings Sync: Turn On"
4. Select settings to sync

### Workspace Settings

Create `.vscode/settings.json`:
```json
{
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100],
    "editor.renderWhitespace": "all",
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.testing.pytestEnabled": true
}
```

## Troubleshooting

### Common Issues

1. Extension Conflicts
   - Disable conflicting extensions
   - Check extension settings
   - Clear extension cache

2. Performance Issues
   - Disable unused extensions
   - Reduce extension features
   - Update extensions

3. Configuration Problems
   - Reset extension settings
   - Check workspace settings
   - Verify file associations

## See Also

- [Environment Setup](environment-setup.md)
- [VS Code Integration](vscode-integration.md)
- [Development Workflow](development-workflow.md)
