# grep.md

## About
**Name:** grep (stands for 'global regular expression print', from the ed editor command g/re/p, meaning 'globally search for a regular expression and print matching lines')

**Created:** Created in 1973 by Ken Thompson for Unix, grep stands for "global regular expression print." Its purpose is to search for patterns in text using regular expressions.

**Similar Technologies:** ack, ag (The Silver Searcher), ripgrep (rg), sed, awk

**Plain Language Definition:**
grep is a command-line tool that lets you quickly search for words or patterns in files or text.

---

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

## Combinations

```bash
# 1. Find Python files using sklearn
find . -name "*.py" | xargs grep -l "sklearn" | head -10

# 2. Find TODO and FIXME comments in Python files
grep -r "TODO\|FIXME" --include="*.py" .
```
