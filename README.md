# Financial Times Themes

A collection of editor and terminal themes inspired by the Financial Times color palette. Includes themes for VSCode, Zed, Sublime Text, Ghostty, and Fish shell.

## Overview

This project generates themes in two variants:
- **Standard**: Light theme with paper background
- **Inverse**: Dark theme with inverted colors

### Accessibility

All themes are designed with accessibility in mind:
- **WCAG AA compliant**: All colors meet the 4.5:1 minimum contrast ratio for normal text
- **Colorblind-friendly**: Green colors are at least 2x brighter than reds (luminance ratio), making them distinguishable for users with deuteranopia or protanopia (red-green color blindness)

## Prerequisites

- Python 3.7 or later
- For VSCode packaging: [vsce](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#vsce) (Visual Studio Code Extension Manager)
  ```bash
  npm install -g @vscode/vsce
  ```

## Quick Start

Build all themes:
```bash
make all
```

Build and install all themes:
```bash
make all.install
```

## Building Themes

### Build All Themes
```bash
make all
```

### Build Individual Themes

#### VSCode
```bash
make vscode
```
Generates:
- `build/vscode/ft-standard.json` - Standard theme definition
- `build/vscode/ft-inverse.json` - Inverse theme definition
- `build/vscode/package.json` - Extension manifest
- `build/vscode/financial-times-theme-0.1.0.vsix` - Installable extension package

#### Zed
```bash
make zed
```
Generates:
- `build/zed/financial-times.json` - Theme file containing both variants

#### Sublime Text
```bash
make sublime
```
Generates:
- `build/sublime/Financial Times Standard.sublime-color-scheme` - Standard theme
- `build/sublime/Financial Times Inverse.sublime-color-scheme` - Inverse theme

#### Ghostty
```bash
make ghostty
```
Generates:
- `build/ghostty/financial-times-standard` - Standard terminal theme
- `build/ghostty/financial-times-inverse` - Inverse terminal theme

#### Fish Shell
```bash
make fish
```
Generates:
- `build/fish/financial-times-standard.theme` - Standard shell theme
- `build/fish/financial-times-inverse.theme` - Inverse shell theme

## Installing Themes

### Install All Themes
```bash
make all.install
```

### Install Individual Themes

#### VSCode
```bash
make vscode.install
```

This installs the `.vsix` extension package. After installation:
1. Open VSCode
2. Press `Cmd+K Cmd+T` (Mac) or `Ctrl+K Ctrl+T` (Windows/Linux)
3. Select either "Financial Times Standard" or "Financial Times Inverse"

**Manual installation:**
```bash
code --install-extension build/vscode/financial-times-theme-0.1.0.vsix
```

#### Zed
```bash
make zed.install
```

This copies the theme to `~/.config/zed/themes/financial-times.json`. After installation:
1. Open Zed
2. Press `Cmd+K Cmd+T` (Mac) or `Ctrl+K Ctrl+T` (Windows/Linux) to open theme selector
3. Select either "Financial Times Standard" or "Financial Times Inverse"

**Manual installation:**
```bash
mkdir -p ~/.config/zed/themes
cp build/zed/financial-times.json ~/.config/zed/themes/
```

#### Sublime Text
```bash
make sublime.install
```

This copies the color schemes to Sublime Text's User packages directory. After installation:
1. Open Sublime Text
2. Go to Preferences > Select Color Scheme
3. Select either "Financial Times Standard" or "Financial Times Inverse"

**Manual installation (macOS):**
```bash
mkdir -p ~/Library/Application\ Support/Sublime\ Text/Packages/User
cp build/sublime/*.sublime-color-scheme ~/Library/Application\ Support/Sublime\ Text/Packages/User/
```

**Manual installation (Linux):**
```bash
mkdir -p ~/.config/sublime-text/Packages/User
cp build/sublime/*.sublime-color-scheme ~/.config/sublime-text/Packages/User/
```

**Manual installation (Windows):**
```powershell
Copy-Item build\sublime\*.sublime-color-scheme "$env:APPDATA\Sublime Text\Packages\User\"
```

#### Ghostty
```bash
make ghostty.install
```

This copies themes to `~/.config/ghostty/themes/`. To use a theme, add this to your `~/.config/ghostty/config`:
```
theme = financial-times-standard
# or
theme = financial-times-inverse
```

**Manual installation:**
```bash
mkdir -p ~/.config/ghostty/themes
cp build/ghostty/financial-times-* ~/.config/ghostty/themes/
```

#### Fish Shell
```bash
make fish.install
```

This copies themes to `~/.config/fish/themes/`. To activate a theme:
```bash
# For standard theme
source ~/.config/fish/themes/financial-times-standard.theme

# For inverse theme
source ~/.config/fish/themes/financial-times-inverse.theme
```

To make it permanent, add the source command to your `~/.config/fish/config.fish`.

**Manual installation:**
```bash
mkdir -p ~/.config/fish/themes
cp build/fish/*.theme ~/.config/fish/themes/
```

## Makefile Targets

| Target | Description |
|--------|-------------|
| `make all` | Build all themes |
| `make all.install` | Build and install all themes |
| `make vscode` | Build VSCode theme |
| `make vscode.install` | Build and install VSCode theme |
| `make zed` | Build Zed theme |
| `make zed.install` | Build and install Zed theme |
| `make sublime` | Build Sublime Text theme |
| `make sublime.install` | Build and install Sublime Text theme |
| `make ghostty` | Build Ghostty theme |
| `make ghostty.install` | Build and install Ghostty theme |
| `make fish` | Build Fish shell theme |
| `make fish.install` | Build and install Fish shell theme |
| `make clean` | Remove all build artifacts |

## Development

Each theme is generated by a Python script:
- `vscode.py` - VSCode theme generator
- `zed_theme.py` - Zed theme generator
- `sublime.py` - Sublime Text theme generator
- `ghostty.py` - Ghostty theme generator
- `fish_theme.py` - Fish shell theme generator
- `ft_palette.py` - Color palette definitions

To modify the colors, edit `ft_palette.py`. To change theme structure, modify the respective generator script.

## License

See LICENSE file for details.
