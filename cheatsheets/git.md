# git.md

## About
**Name:** Git (the name was chosen by its creator, Linus Torvalds, as a self-deprecating joke; "git" is British slang for an unpleasant person, and Torvalds wanted a short, unique, and memorable name.)

**Created:** Git was created in 2005 by Linus Torvalds to manage the development of the Linux kernel after a dispute with the maintainers of BitKeeper, a proprietary version control system. Its purpose is to provide a fast, distributed, and robust version control system for tracking changes in source code during software development.

**Similar Technologies:** Mercurial, Subversion (SVN), Perforce, CVS, Bazaar

**Plain Language Definition:**
Git is a tool that helps you keep track of changes to your files and collaborate with others. It lets you save versions of your work, go back to previous versions, and work with teammates without overwriting each other's changes.

---

# High level intro to git

## A basic overview

### Git is not easy

The following language is somewhat inaccurate in order to present a quick, simplified intro.

This is written with the expectation that before using git, you'll pursue additional learning.

### Version control

Version control allows you to track changes to files and manage different versions of your project. This makes it easier to collaborate with others.

It's like a multi-dimensional time machine for your project.

### Git - Distributed VCS

Git is a software solution. You can use it in many programs or directly in terminal.

It's a "distributed version control system" that allows you to work on your project locally, and maintain a history of file changes.

### .git/

The mechanisms of each git project are contained within a `.git` folder in your project's directory.

Starting out, simply think of it as a black box that each project needs.

### Repository, aka repo

A repo is like a folder that contains all files and the history of a project. It's the place where your project is stored.

### Local and Remote repos

Git is distributed. Data (your code) can be stored in multiple places.

#### Local

The local repo is on your (DOVE) computer. It's on the filesystem, where you write and run your code. It's just a local directory, which contains a `.git` folder.

#### Remote

This is hosted on a remote server. For us, this is a central hub (GitLab) where we upload local files to. 

It's a bit like Sharepoint, but for code.

### Clone - copying a repo to local

Cloning a repo means copying code from a remote repo to your local computer. This allows you to work on a project.

`git clone https://....`

### Commit

You can commit code to create a save state. As such, you can checkout (load) earlier versions of the code. 

Think time traveling.

### Push

When you want to send your local changes to GitLab, you `push`.

### Pull

When you want to download changes from GitLab, you `pull`.

### Branch for parallel development

Git allows you to create branches, which are separate lines of development.

You can work on new additions to the code in isolation, making it easier to manage your project. When everything looks good, you can merge this change branch into the existing code base.

Maybe it's like traveling across dimensions?

### Git is not easy

Most people do not learn git in a week, or even a year.

Learning git is much easier while working on solo projects. 

Jumping straight into a collaborative project is more difficult.

### Failsafe approach

xcid comic

## Basic Operations

```bash
git init                     # Initialize new repository
git clone url                # Clone remote repository
git status                   # Show working directory status
git add file                 # Stage specific file
git add .                    # Stage all changes
git commit -m "message"      # Commit staged changes
git commit -am "message"     # Stage and commit all changes
```

## Branching & Merging

```bash
git branch                   # List local branches
git branch -a                # List all branches (local + remote)
git branch feature-branch    # Create new branch
git checkout branch-name     # Switch to branch
git checkout -b new-branch   # Create and switch to new branch
git merge feature-branch     # Merge branch into current
git branch -d branch-name    # Delete local branch
```

## Remote Operations

```bash
git remote -v                # Show remote repositories
git fetch                    # Fetch changes from remote
git pull                     # Fetch and merge remote changes
git push                     # Push changes to remote
git push -u origin branch    # Push and set upstream
git push --force-with-lease  # Safer force push
```

## History & Inspection

```bash
git log                      # Show commit history
git log --oneline            # Compact commit history
git log --graph --oneline    # Visual branch history
git log --pretty=format:"%h %an %ar - %s"  # Custom format
git log --pretty=oneline     # One line per commit
git log --pretty=short       # Short format
git log --pretty=full        # Full format
git log --graph --pretty=format:"%C(yellow)%h%Creset -%C(red)%d%Creset %s %C(green)(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit  # Colorful graph
git log --since="2 weeks ago"  # Commits since date
git log --until="yesterday"  # Commits until date
git log --author="John"      # Commits by author
git log -p                   # Show patches/diffs
git log --stat               # Show file statistics
git log --name-only          # Show only file names
git log --follow filename    # Follow file renames
git show commit-hash         # Show specific commit details
git diff                     # Show unstaged changes
git diff --staged            # Show staged changes
git diff HEAD~1              # Compare with previous commit
git diff branch1..branch2    # Compare branches
git blame file               # Show who changed each line
git show --name-only HEAD    # Show files in last commit
```

## Git Status & Porcelain

```bash
git status                   # Show working directory status
git status -s                # Short status format
git status --porcelain       # Machine-readable status
git status --porcelain=v2    # Enhanced porcelain format
git status -b                # Show branch info
git status --ignored         # Show ignored files too
git status --untracked-files=all  # Show all untracked files
```

## Advanced Log Formatting

```bash
# Custom log with hash, author, date, and message
git log --pretty=format:"%h - %an, %ar : %s"

# Show commits with file changes
git log --name-status

# Show commits affecting specific file
git log --follow -- filename

# Show merge commits only
git log --merges

# Show commits between tags/branches
git log tag1..tag2
git log main..feature-branch

# Show commits with word diff
git log -p --word-diff

# Show commits in last 5 days with author
git log --since="5 days ago" --pretty=format:"%h %an %s"
```

## Data Science Workflow

```bash
# 1. Create feature branch
git checkout -b feature/new-model

# 2. Add and commit changes
git add notebooks/ src/ requirements.txt
git commit -m "feat: implement XGBoost model"

# 3. Push feature branch
git push -u origin feature/new-model

# 4. Merge back to main
git checkout main && git pull && git merge feature/new-model
```
