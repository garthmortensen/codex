# commitizen.md

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
