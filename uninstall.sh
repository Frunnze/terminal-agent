#!/bin/bash
venv/bin/pip uninstall terminal-agent -y
sed -i '' '/alias agent=/d' ~/.zshrc
rm -rf venv
echo "Done. Restart your terminal for the alias to be removed."
