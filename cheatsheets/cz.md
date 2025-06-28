# cz.md

## About
**Name:** Commitizen (cz) - named for helping developers become "citizens" of consistent commit practices.

**Created:** Developed to standardize commit messages and automate versioning in software projects. It emerged from the need to make git commit histories more readable and meaningful, especially in teams where different developers had varying commit message styles.

**Similar Technologies:** Conventional Commits, semantic-release, git hooks, husky, lint-staged, standard-version

**Plain Language Definition:** Commitizen is a tool that guides you through creating well-formatted commit messages. It's like having a template that ensures everyone on your team writes git commits in the same clear, organized way, making it easier to track changes and automatically generate release notes.

---

# cz.md

## Commit Operations

```bash
cz commit                   # Interactive commit wizard
cz c                        # Short form of commit
cz commit --dry-run         # Preview commit message
cz commit --retry           # Retry last commit
```

## Versioning & Changelog

```bash
cz bump                     # Auto bump version
cz bump --dry-run           # Preview version bump
cz bump --increment PATCH   # Bump patch version
cz bump --increment MINOR   # Bump minor version
cz bump --increment MAJOR   # Bump major version
cz changelog                # Generate changelog
```

## Information & Setup

```bash
cz info                     # Show current config
cz example                  # Show commit examples
cz schema                   # Show commit schema
cz init                     # Initialize commitizen
cz --version                # Show version
```

## Configuration

```bash
cz --name cz_conventional_commits  # Set commit style
cz check --commit-msg-file    # Check commit message
cz check --rev-range          # Check commit range
```

## Common Commit Types

| Type | Description | Example |
|------|-------------|---------|
| **feat** | new feature | feat: add user authentication |
| **fix** | bug fix | fix: resolve login error |
| **docs** | documentation | docs: update API documentation |
| **style** | formatting | style: fix code formatting |
| **refactor** | refactor | refactor: optimize data processing |
| **test** | add tests | test: add unit tests for auth |
| **chore** | maintenance | chore: update dependencies |
| **perf** | performance | perf: improve query performance |
| **ci** | CI/CD changes | ci: add automated testing |
