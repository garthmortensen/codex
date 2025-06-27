
#!/bin/bash
# === FILE META OPENING ===
# file: ~/cheatsheets/cheatsheets.sh
# desc: simplified launcher for python-based cheatsheet manager
# === FILE META CLOSING ===

# Directory containing cheatsheet files
CHEATSHEETS_DIR="$HOME/cheatsheets"

# Main function that launches the Python cheatsheet manager using uv
cheats_menu_select() {
    cd "$CHEATSHEETS_DIR"
    uv run cheatsheets "$CHEATSHEETS_DIR"
}

# If script is called directly, run the function
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    cheats_menu_select
fi
