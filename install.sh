#!/bin/bash
python3 -m venv venv
venv/bin/pip install -e .
echo "alias agent='$PWD/venv/bin/agent'" >> ~/.zshrc
echo "Done. Restart your terminal."
