# grep.md

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

## Data Science Power Combinations

```bash
# 1. Find Python files using sklearn
find . -name "*.py" | xargs grep -l "sklearn" | head -10

# 2. Find TODO and FIXME comments in Python files
grep -r "TODO\|FIXME" --include="*.py" .
```
