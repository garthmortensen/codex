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
git show commit-hash         # Show specific commit details
git diff                     # Show unstaged changes
git diff --staged            # Show staged changes
git blame file               # Show who changed each line
```

## Undoing Changes

```bash
git reset HEAD file          # Unstage file
git checkout -- file         # Discard changes to file
git reset --soft HEAD~1      # Undo last commit, keep changes
git reset --hard HEAD~1      # Undo last commit, discard changes
git revert commit-hash       # Create new commit undoing changes
git stash                    # Temporarily save changes
git stash pop                # Apply and remove latest stash
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
