# VS Code Extensions

This guide covers the recommended VS Code extensions for the prototype environment and how to use them effectively.

## Core Extensions

### Python Development

1. **Python** (ms-python.python)
   - IntelliSense
   - Linting
   - Debugging
   - Testing
   - Jupyter support
   ```json
   "python.formatting.provider": "black",
   "python.linting.enabled": true
   ```

2. **Pylance** (ms-python.vscode-pylance)
   - Type checking
   - Import organization
   - Advanced IntelliSense
   ```json
   "python.analysis.typeCheckingMode": "basic",
   "python.analysis.diagnosticMode": "workspace"
   ```

3. **Python Test Explorer** (littlefoxteam.vscode-python-test-adapter)
   - Visual test runner
   - Test discovery
   - Test debugging
   ```json
   "pythonTestExplorer.testFramework": "pytest"
   ```

### Documentation

1. **Markdown All in One** (yzhang.markdown-all-in-one)
   - Table of contents
   - Auto-formatting
   - Math equations
   ```json
   "markdown.extension.toc.updateOnSave": true,
   "markdown.extension.preview.autoShowPreviewToSide": true
   ```

2. **reStructuredText** (lextudio.restructuredtext)
   - Syntax highlighting
   - Preview
   - IntelliSense
   ```json
   "restructuredtext.confPath": "${workspaceFolder}/docs"
   ```

### Git Integration

1. **GitLens** (eamodio.gitlens)
   - Blame annotations
   - Repository visualization
   - History exploration
   ```json
   "gitlens.codeLens.enabled": true,
   "gitlens.currentLine.enabled": true
   ```

2. **GitHub Pull Requests** (github.vscode-pull-request-github)
   - PR management
   - Review tools
   - Issue tracking
   ```json
   "githubPullRequests.createOnPublish": "ask"
   ```

## Productivity Extensions

### Code Quality

1. **Error Lens** (usernamehw.errorlens)
   - Inline error display
   - Quick fixes
   - Enhanced diagnostics
   ```json
   "errorLens.enabledDiagnosticLevels": [
     "error",
     "warning",
     "info"
   ]
   ```

2. **Code Spell Checker** (streetsidesoftware.code-spell-checker)
   - Spell checking
   - Custom dictionaries
   - Multi-language support
   ```json
   "cSpell.enableFiletypes": [
     "python",
     "markdown",
     "yaml"
   ]
   ```

### Navigation

1. **Path Intellisense** (christian-kohler.path-intellisense)
   - Path completion
   - Import suggestions
   ```json
   "path-intellisense.autoSlashAfterDirectory": true
   ```

2. **Todo Tree** (gruntfuggly.todo-tree)
   - TODO comment tracking
   - Custom tags
   - Tree view
   ```json
   "todo-tree.general.tags": [
     "TODO",
     "FIXME",
     "NOTE",
     "HACK"
   ]
   ```

### Editor Enhancement

1. **Better Comments** (aaron-bond.better-comments)
   - Comment highlighting
   - Custom tags
   ```json
   "better-comments.tags": [
     {
       "tag": "!",
       "color": "#FF2D00",
       "strikethrough": false,
       "backgroundColor": "transparent"
     }
   ]
   ```

2. **Bracket Pair Colorizer 2** (coenraads.bracket-pair-colorizer-2)
   - Bracket matching
   - Custom colors
   ```json
   "bracket-pair-colorizer-2.colors": [
     "#fafafa",
     "#9F51B6",
     "#F7C244"
   ]
   ```

## Theme Extensions

### UI Themes

1. **Material Icon Theme** (pkief.material-icon-theme)
   - File icons
   - Folder icons
   ```json
   "workbench.iconTheme": "material-icon-theme",
   "material-icon-theme.activeIconPack": "react"
   ```

2. **Atom One Dark Theme** (akamud.vscode-theme-onedark)
   - Dark theme
   - Syntax highlighting
   ```json
   "workbench.colorTheme": "Atom One Dark"
   ```

## Extension Management

### Installation

1. Bulk Install:
   ```bash
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   ```

2. Extensions File:
   ```json
   // .vscode/extensions.json
   {
     "recommendations": [
       "ms-python.python",
       "ms-python.vscode-pylance",
       "littlefoxteam.vscode-python-test-adapter"
     ]
   }
   ```

### Configuration

Create workspace settings:

```json
// .vscode/settings.json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "files.trimTrailingWhitespace": true
}
```

## Best Practices

1. Extension Usage:
   - Install only needed extensions
   - Configure per-workspace settings
   - Use extension packs

2. Performance:
   - Disable unused extensions
   - Configure appropriate resource usage
   - Monitor extension impact

3. Updates:
   - Keep extensions updated
   - Review changelogs
   - Test after major updates

## Troubleshooting

### Common Issues

1. Extension Conflicts:
   - Disable conflicting extensions
   - Check extension logs
   - Reset extension settings

2. Performance Issues:
   - Use "Developer: Show Running Extensions"
   - Disable heavy extensions
   - Clear extension cache

### Getting Help

- Extension documentation
- GitHub issues
- VS Code community

## Next Steps

- Review [VS Code Integration](vscode-integration.md)
- Explore [Development Workflow](development-workflow.md)
- Check [Code Style](../best-practices/code-style.md)
