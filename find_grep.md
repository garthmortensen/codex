# find_grep.md

## Find - File Discovery

```bash
find . -name "*.py"            # Find Python files
find . -type f -size +100M     # Find large files (>100MB)
find . -mtime -7               # Files modified in last 7 days
find . -name "*.log" -delete   # Find and delete log files
find . -type d -empty          # Find empty directories
find . -perm 777               # Find files with 777 permissions
find . -user $USER             # Find files owned by current user
```

## Find with Exec & Xargs

```bash
# Find Python files containing pandas import
find . -name "*.py" -exec grep -l "import pandas" {} \;
find . -name "*.py" | xargs grep -l "import pandas"

# Remove compiled Python files
find . -type f -name "*.pyc" | xargs rm

# Count lines in Python files
find . -name "*.py" | xargs wc -l

# Handle filenames with spaces
find . -name "*.py" -print0 | xargs -0 grep "TODO"
```

## Grep - Pattern Matching

```bash
grep -r "function" .          # Recursive search in directory
grep -i "error" logfile       # Case-insensitive search
grep -v "debug" logfile       # Exclude lines with 'debug'
grep -n "TODO" *.py           # Show line numbers
grep -A 3 -B 2 "error" log    # Show 3 lines after, 2 before
grep -c "import" *.py         # Count occurrences
grep -E "(error|warning)" log  # Extended regex (OR)
grep -l "pandas" *.py         # Show only filenames
```

## Sed - Stream Editor

```bash
sed 's/old/new/g' file         # Replace all occurrences
sed -i 's/old/new/g' file      # In-place replacement
sed '5d' file                  # Delete line 5
sed '1,5d' file                # Delete lines 1-5
sed '/pattern/d' file          # Delete lines containing pattern
sed -n '10,20p' file           # Print lines 10-20
sed 's/^/  /' file             # Add 2 spaces to start of each line
sed '/pattern/a\new line' file # Add line after pattern match
```

## Awk - Text Processing

```bash
awk '{print $1}' file          # Print first column
awk -F: '{print $1}' /etc/passwd # Use colon as delimiter
awk '$3 > 50' data.txt        # Print lines where column 3 > 50
awk '{sum += $1} END {print sum}' file # Sum first column
awk 'length > 80' file         # Print lines longer than 80 chars
awk '/pattern/ {print $2}' file # Print col 2 of lines with pattern
awk '{print NF, $0}' file     # Print number of fields per line
```

## Data Science Power Combinations

```bash
# 1. Find Python files using sklearn
find . -name "*.py" | xargs grep -l "sklearn" | head -10

# 2. Count lines in CSV files, sorted by size
find . -name "*.csv" -exec wc -l {} + | sort -n

# 3. Find TODO and FIXME comments in Python files
grep -r "TODO\|FIXME" --include="*.py" .

# 4. List all function definitions with filenames
find . -name "*.py" | xargs awk '/^def / {print FILENAME ": " $0}'

# 5. Extract class definitions (no comments)
sed -n '/class /,/def /p' *.py | grep -v "^#"
```
