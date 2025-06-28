# linux.md

## Search & Find

```bash
grep -r "pattern" /path        # Search recursively for a pattern in a directory
grep -i "pattern" file         # Case-insensitive search
grep -n "pattern" file         # Show line numbers in results
grep -v "pattern" file         # Invert match (exclude pattern)
find /path -name "*.txt"      # Find files by name pattern
find /path -type f -size +10M  # Find files larger than 10MB
find /path -mtime -7           # Find files modified in last 7 days
find /path -exec chmod 644 {} \; # Execute command on found files
```

## Text Processing

```bash
awk '{print $1}' file          # Print first column
awk -F: '{print $1}' /etc/passwd # Use colon as field separator
sed 's/old/new/g' file         # Replace all occurrences
sed -i 's/old/new/g' file      # Replace in-place (modify file)
cut -d: -f1 /etc/passwd        # Cut first field (colon delimiter)
sort file | uniq               # Sort and remove duplicates
sort -k2 -n file               # Sort by second column numerically
```

## Process Management

```bash
ps aux                      # List all running processes
pgrep -f process_name          # Get PID by process name
pkill -f process_name          # Kill process by name
kill -9 PID                    # Force kill process
nohup command &                # Run command in background
jobs                           # List background jobs
fg %1                          # Bring job 1 to foreground
```

## File Permissions

```bash
chmod +x /path/to/file      # Make a file executable
chmod 755 file                  # Set permissions (rwxr-xr-x)
chmod -R 644 /path              # Set permissions recursively
chown user:group file           # Change owner and group
chown -R user:group /path       # Change ownership recursively
umask 022                       # Set default permissions
```

## Networking

```bash
ip addr show                # Show IP addresses
netstat -tuln                 # Show listening ports
ss -tuln                      # Modern netstat alternative
lsof -i :80                   # Show processes using port 80
```

## System Information

```bash
uname -a                    # Show kernel and system info
htop                          # Interactive process viewer
du -sh /*                     # Show directory sizes
watch -n 1 'command'          # Run command every second
```

## Archives & Compression

```bash
tar -czvf archive.tar.gz /path/to/dir  # Create a compressed tarball
tar -xzf archive.tar.gz        # Extract compressed archive
tar -tzf archive.tar.gz        # List archive contents
zip -r archive.zip /path       # Create zip archive
unzip archive.zip              # Extract zip archive
gzip file                      # Compress single file
gunzip file.gz                 # Decompress gzipped file
```

## Ssh (Secure Shell)

```bash
ssh user@host               # Connect to a remote host
scp file user@host:/path    # Copy file to remote host
sftp user@host               # Secure FTP to remote host
```

## Power User Combinations

```bash
# 1. Find log files with errors
find /var/log -name "*.log" -exec grep -l "error" {} \;

# 2. Show processes with PID and command
ps aux | awk '{print $2, $11}' | sort -k2

# 3. Find and delete temp files
find /home -type f -name "*.tmp" -delete

# 4. Create dated backup
tar -czf backup-$(date +%Y%m%d).tar.gz /important/data
```