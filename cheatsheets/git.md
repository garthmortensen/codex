# git.md

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
