#!/bin/bash

# Install zsh
echo "Installing zsh..."
brew install zsh

# Install oh-my-zsh
echo "Installing oh-my-zsh..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Add plugins to oh-my-zsh
echo "Adding plugins..."
sed -i '' 's/plugins=(git)/plugins=(git docker python)/g' ~/.zshrc

# Set zsh as the default shell
echo "Setting zsh as the default shell..."
chsh -s /bin/zsh

echo "Installation complete. Please restart your terminal."
