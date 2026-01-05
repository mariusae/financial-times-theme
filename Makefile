.PHONY: all all.install clean vscode vscode.install zed zed.install ghostty ghostty.install fish fish.install sublime sublime.install

# VSCode binary (override with CODE=... make vscode.install)
CODE ?= code

# Build all themes
all: vscode zed ghostty fish sublime

# Build and install all themes
all.install: vscode.install zed.install ghostty.install fish.install sublime.install

# VSCode targets
vscode:
	@echo "Building VSCode theme..."
	python3 vscode.py

vscode.install: vscode
	@echo "Installing VSCode theme..."
	$(CODE) --install-extension build/vscode/financial-times-theme-0.1.0.vsix

# Zed targets
zed:
	@echo "Building Zed theme..."
	python3 zed_theme.py

zed.install: zed
	@echo "Installing Zed theme..."
	@mkdir -p ~/.config/zed/themes
	cp build/zed/financial-times.json ~/.config/zed/themes/
	@echo "Zed theme installed to ~/.config/zed/themes/financial-times.json"

# Ghostty targets
ghostty:
	@echo "Building Ghostty theme..."
	python3 ghostty.py

ghostty.install: ghostty
	@echo "Installing Ghostty theme..."
	@mkdir -p ~/.config/ghostty/themes
	cp build/ghostty/financial-times-* ~/.config/ghostty/themes/
	@echo "Ghostty themes installed to ~/.config/ghostty/themes/"
	@echo "Add 'theme = financial-times-standard' or 'theme = financial-times-inverse' to ~/.config/ghostty/config"

# Fish shell targets
fish:
	@echo "Building Fish shell theme..."
	python3 fish_theme.py

fish.install: fish
	@echo "Installing Fish shell theme..."
	@mkdir -p ~/.config/fish/themes
	cp build/fish/*.theme ~/.config/fish/themes/
	@echo "Fish themes installed to ~/.config/fish/themes/"
	@echo "Source the theme in your config.fish:"
	@echo "  source ~/.config/fish/themes/financial-times-standard.theme"
	@echo "  or"
	@echo "  source ~/.config/fish/themes/financial-times-inverse.theme"

# Sublime Text targets
sublime:
	@echo "Building Sublime Text theme..."
	python3 sublime.py

sublime.install: sublime
	@echo "Installing Sublime Text theme..."
	@mkdir -p ~/Library/Application\ Support/Sublime\ Text/Packages/User
	cp build/sublime/*.sublime-color-scheme ~/Library/Application\ Support/Sublime\ Text/Packages/User/
	@echo "Sublime Text themes installed to ~/Library/Application Support/Sublime Text/Packages/User/"
	@echo "To activate: Preferences > Select Color Scheme > Financial Times Standard/Inverse"

# Clean build artifacts
clean:
	@echo "Cleaning build directory..."
	rm -rf build/
	@echo "Build artifacts removed"
