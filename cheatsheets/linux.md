# linux.md

## About
**Name:** Linux (named after its creator, Linus Torvalds, combined with 'Unix' to reflect its Unix-like design. The name was suggested by Ariane van der Steldt, a friend of Torvalds.)

**Created:** Linux was created in 1991 by Linus Torvalds as a free, open-source operating system kernel inspired by Unix. Its purpose is to provide a stable, secure, and flexible foundation for operating systems on computers, servers, and devices worldwide.

**Similar Technologies:** Unix, BSD, Solaris, Windows, macOS

**Plain Language Definition:**
Linux is a free operating system that runs on everything from laptops to supercomputers. It's known for being reliable, secure, and customizable, and is widely used by developers and companies around the world.

---

# Linux Overview

## Why important

Over 80% of web servers run on [unix](https://w3techs.com/technologies/overview/operating_system/all), which was created by AT&T Bell Labs. Unix and Windows were not free and not easily accessible. Linux made everything free, and was aimed at researchers and students.

Linus Torvalds created Linux (and git!), and is an open source unix-like kernel.

Common roles that use linux are Help Desk/IT, sysadmin, security, network analysts.

## Intro ideas

Typically, most servers dont have GUI. GUI vs UI? A command line interface (CLI) counts as a user interface, but does not contain graphics so is not a GUI. CLI-only servers are "headless" servers. Server? Because many computers can access it simultaneously. With a Linux or Windows server, many people can login and use the hardware simultaneously.

physical and virtual machines. Physical, aka bare metal machines. One physical can run many virtual. Virtualization was around at least late 90s/early 2000s when you would download images of software and mount in virtual drives.

Kernel is the core of any OS. It manages your memory, processes, tasks, disk. It's the middle layer between your hardware and any software.  A shell wraps around the kernel, letting you talk to your OS. 

Bash (Bourne Again Shell) = the default shell for most linux distros. 

cmd/powershell (ps) = ... for Windows

Bash is good for unix, linux, mac, git bash, WSL.

## Linux distros

There are many distributions:

https://en.wikipedia.org/wiki/Linux_distribution#/media/File:Linux_Distribution_Timeline_21_10_2021.svg

Common distros include:

- Debian (apt-get). 
  - Apt = aptitude, the package manager for ubuntu. You install things from databases, referred to as repos. You can have main repos, satellite repos, etc.
  - Other distros use yum, rpm, pkg, apt-get, ...

- Ubuntu = most flexible, best for day to day tasks. A good linux desktop environment. Has email client, web browser, text editor, etc.
- Kali = security, penetration testing.
- Red hat
  - Fedora
  - CentOS
  - Red Hat Enterprise Linux (REHL) = relatively more difficult to use.
  - Scientific Linux

Stable versions = Long Term Support (LTS) versions. Only changes once per year, or less often. REHL is every ~2-4 years.

Faster changing distros have more vulnerabilities.

And, all variations have a headless version.

## File system (fs)

Sysadmins seem to have their own take on these directories. 

/ = root. Only contains crucial directories. Base files in / are suspicious.

/home = private user folders. Usually where your write access is limited to.

/etc = config files, e.g. users and passwords

/bin, /sbin = binaries. Applications, web browsers, commands like `ls`. think /program files/

/var = dir for files that change over time, variable files. /var/log. Logs are meant to last forever. You append to them, not overwrite them. They're variable files, not temporary.

/tmp = short lived files. 

## Common commands

- pwd = current working directory
- ls = list files and directories
- cd = navigate directories
- mkdir = make directory
- rmdir = remove directory
- rm = remove file
- touch = create file `<command> <argument>` = `touch file1.txt`
- clear = clear terminal

## Paths

Absolute paths

`/home/garth/whatever`

Relative paths

`./garth/whatever2`

"Dot slash"

## Program usage

### `cp`

`<program name> <file> <desination>`

### `mv`

`mv /dir1/file1.csv /dir2/file1.csv`

## Practice

1. Make a folder. Folder? Dir?
2. Create a file.
3. Make another folder
4. Make another folder
5. Copy the file to one folder
6. Move the file to another folder

## More linux commands

- less = less
- more = more
- cat = concatenate `cat file1.txt file2.txt`
- man = manual. `man ls`
- head = `head -5 cats.txt`
- tail = `tail -5 cats.txt`

## Carrots

`cat file1.txt file2.txt > both.txt`

input data = argument, aka `stdin`

output data = return, aka `stdout`

`cat file1.txt file2.txt > both.txt`

## Commands, take 2

`ls` is the command

`-a` is the option (case sensitive)

Options that require their their own arguments = parameters.

`head -n 5 cats.txt`

`cat` is the command

`-n` is the option

`5` is the parameter

`5` is the parameter for option `-n`

`su` switch user = `su gandalf`

`sudo` super user do = `sudo apt install`

`id` = might return your employee id numbers

## Otherwise

Linux has tons of useful commands.

`wc -w *` = does wordcount on entire directory.

 `wc -w * > output.txt`

 `wc -l * > output.txt` = lower L shows the line numbers

## Searching for things

`find -type f -iname something.txt`

`find -type f -iname *.txt` = iname is insensitive to typecase

`find -type f -iname *cats* -o *dogs*` = find files which contain the words cats or dogs

`find -type d -iname _logs` = do it with directories too

## Searching within files for things

grep = global regular expression printer

https://www.youtube.com/watch?v=528Jc3q86F8

`<grep string search>`

`grep ERROR output.log`

`grep ERROR *.log`

`grep -i error *.log` = typecase insensitive

`grep -il error *.log` = lower L = return only the filename

## Cool pipes

Run one command, and redirect the output to another command.

You can pipe, pipe, pipe, but only from left to right.

`grep -il error *.log | wc -l` = shows the line numbers error appears on

## Scripting

Instead of running these commands step by step, we can string them together.

```bash
# touch myscript.sh

#!/bin/bash  # tells linux to run this script with the bash shell, and creates a log in that dir so we can see when scripts run

mkdir dogs
cd dogs

# sh myscript.sh
```

You can also pass arguments into shell scripts.

```bash
# touch myscript2.sh

#!/bin/bash

mkdir $1
cd $1

# sh myscript2.sh cats
```

## Example

https://github.com/garthmortensen/code_club/blob/master/create_env.sh

Readme.md

`./create_env.sh`

https://github.com/garthmortensen/update_setup_files/blob/main/update_setup_files.sh

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