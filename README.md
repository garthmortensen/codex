# README.md

Cheatsheet Manager is a CL tool for organizing, searching, and displaying technical cheatsheets for quick reference.

## First Time Setup

1. clone:
   ```bash
   git clone https://github.com/yourusername/cheatsheets.git
   cd cheatsheets
   ```

1. install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

1. for quick access, add alias to your shell (`.bashrc` or `.zshrc`):
   ```bash
   alias cheat='cd ~/cheatsheets && uv run python src/cheatsheets/app.py'
   ```
