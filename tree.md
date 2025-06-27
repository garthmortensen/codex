# tree.md

## Basic Usage

```bash
tree                        # Show directory tree
tree /path                  # Show tree for specific path
tree -a                     # Include hidden files
tree -d                     # Show only directories
tree -f                     # Print full path prefix
tree -L 2                   # Limit depth to 2 levels
tree -P "*.py"             # Show only Python files
tree -I "*.pyc|__pycache__" # Ignore patterns
```

## Output Formatting

```bash
tree -C                     # Colorize output
tree -n                     # Turn off colorization
tree --charset ascii        # Use ASCII characters
tree -Q                     # Quote filenames with spaces
tree -h                     # Print sizes in human readable format
tree -s                     # Print size of each file
tree -D                     # Print last modification date
```

## File Filtering

```bash
tree --filelimit 15         # Don't descend dirs with >15 files
tree --dirsfirst            # List directories before files
tree -t                     # Sort by modification time
tree -r                     # Reverse sort order
tree --du                   # Print directory sizes
```

## Output Formats

```bash
tree -H baseHREF            # Generate HTML output
tree -X                     # Generate XML output
tree -J                     # Generate JSON output
tree -o filename            # Send output to filename
```

## Data Science Project Examples

```bash
# 1. Ignore Python cache and git files
tree -I '__pycache__|*.pyc|.git|.venv'

# 2. Show only code and config files
tree -P '*.py|*.ipynb|*.yml|*.yaml' -I '.git'

# 3. Show structure with file sizes, directories first
tree -L 3 --dirsfirst -h

# 4. Export project structure as JSON
tree -J -o project_structure.json
```
