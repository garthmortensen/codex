# find.md

## Basic Syntax

```bash
find [path] [expression]
find /path/to/search -name "pattern"
```

## Find by Name

```bash
find . -name "*.txt"                    # Find all .txt files
find . -name "*.log" -o -name "*.tmp"   # Find .log OR .tmp files
find . -iname "*.PDF"                   # Case-insensitive name search
find . -name "*config*"                 # Files containing "config"
find . -name "file?.txt"                # Single character wildcard
find . -regex ".*\.(jpg|png|gif)$"      # Using regex patterns
```

## Find by Type

```bash
find . -type f                          # Files only
find . -type d                          # Directories only
find . -type l                          # Symbolic links only
find . -type f -name "*.sh"             # Executable scripts
find . -type d -name ".*"               # Hidden directories
```

## Find by Size

```bash
find . -size +10M                       # Files larger than 10MB
find . -size -1k                        # Files smaller than 1KB
find . -size 100c                       # Files exactly 100 bytes
find . -size +1G -size -2G              # Files between 1GB and 2GB
find . -empty                           # Empty files and directories
find . -type f -size 0                  # Empty files only
```

## Find by Time

```bash
find . -mtime -7                        # Modified in last 7 days
find . -mtime +30                       # Modified more than 30 days ago
find . -atime -1                        # Accessed in last 24 hours
find . -ctime +7                        # Changed more than 7 days ago
find . -newer file.txt                  # Newer than file.txt
find . -newermt "2024-01-01"            # Modified after date
find . -mmin -60                        # Modified in last 60 minutes
```

## Find by Permissions

```bash
find . -perm 755                        # Exact permissions
find . -perm -644                       # At least these permissions
find . -perm /u+w                       # User writable
find . -perm -u=rwx                     # User has read, write, execute
find . -executable                      # Executable files
find . -readable                        # Readable files
find . -writable                        # Writable files
```

## Find by Owner

```bash
find . -user john                       # Files owned by user john
find . -group developers                # Files owned by group developers
find . -uid 1000                        # Files with specific user ID
find . -gid 100                         # Files with specific group ID
find . -nouser                          # Files with no valid user
find . -nogroup                         # Files with no valid group
```

## Execute Commands on Results

```bash
find . -name "*.tmp" -delete            # Delete all .tmp files
find . -name "*.log" -exec rm {} \;     # Delete using exec
find . -name "*.txt" -exec cp {} backup/ \;  # Copy files
find . -type f -exec chmod 644 {} \;    # Change permissions
find . -name "*.py" -exec grep -l "import os" {} \;  # Search in files
find . -name "*.jpg" -exec ls -la {} +  # List details (efficient)
```

## Advanced Examples

```bash
# Find and count files by extension
find . -name "*.py" | wc -l

# Find duplicate files by size
find . -type f -exec du -b {} + | sort -n | uniq -d -w10

# Find largest files in directory
find . -type f -exec ls -la {} + | sort -k5 -nr | head -10

# Find files modified today
find . -type f -newermt $(date +%Y-%m-%d)

# Find broken symbolic links
find . -type l ! -exec test -e {} \; -print

# Find files with specific content
find . -type f -exec grep -l "TODO" {} +

# Find and archive old logs
find /var/log -name "*.log" -mtime +30 -exec tar -czf old_logs.tar.gz {} +
```

## Exclude Patterns

```bash
find . -name "*.txt" ! -path "*/.*"     # Exclude hidden directories
find . -type f ! -name "*.tmp"          # Exclude .tmp files
find . -type f ! -path "*/node_modules/*"  # Exclude node_modules
find . -name "*.py" ! -path "*/venv/*"  # Exclude virtual environments
find . -type f -not -user root          # Exclude files owned by root
```

## Performance Tips

```bash
# Use -prune to skip directories entirely
find . -name ".git" -prune -o -name "*.py" -print

# Limit depth to avoid deep recursion
find . -maxdepth 3 -name "*.conf"

# Use -quit to stop after first match
find . -name "config.txt" -quit

# Combine with xargs for better performance
find . -name "*.log" -print0 | xargs -0 rm

# Use -O2 or -O3 for optimization
find -O3 . -name "*.txt"
```

## Common Use Cases

```bash
# Clean up temporary files
find /tmp -type f -mtime +7 -delete

# Find configuration files
find /etc -name "*.conf" -o -name "*.cfg"

# Find recently modified source code
find . -name "*.py" -o -name "*.js" -mtime -1

# Find large files consuming disk space
find / -type f -size +100M 2>/dev/null

# Find world-writable files (security)
find / -type f -perm -002 2>/dev/null

# Find files without proper ownership
find /home -nouser -o -nogroup 2>/dev/null

# Backup recent changes
find . -type f -mtime -1 -exec cp --parents {} /backup/ \;
```

## Error Handling

```bash
find . -name "*.txt" 2>/dev/null        # Suppress error messages
find . -name "*.txt" 2>&1 | grep -v "Permission denied"  # Filter errors
find . -name "*.txt" -readable          # Only search readable files
```

## Combining with Other Commands

```bash
# Find and compress
find . -name "*.log" -exec gzip {} \;

# Find and move
find . -name "*.bak" -exec mv {} /backup/ \;

# Find and check file types
find . -type f -exec file {} \; | grep "text"

# Find and calculate total size
find . -name "*.pdf" -exec du -ch {} + | tail -1

# Find and create directory structure
find source/ -type d -exec mkdir -p dest/{} \;
```

