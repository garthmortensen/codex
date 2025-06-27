# cheatsheets

These are imported into .zshrc and called via alias

requires `dnf install bat`!

## tree.md

```markdown
----------------------------------------------------------------
| TREE CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC USAGE

```bash
tree                        # Show directory tree
tree /path                  # Show tree for specific path
tree -a                     # Include hidden files
tree -d                     # Show only directories
tree -f                     # Print full path prefix
tree -L 2                   # Limit depth to 2 levels
tree -P "*.py"             # Show only Python files
tree -I "*.pyc|__pycache__" # Ignore patterns
```

## OUTPUT FORMATTING

```bash
tree -C                     # Colorize output
tree -n                     # Turn off colorization
tree --charset ascii        # Use ASCII characters
tree -Q                     # Quote filenames with spaces
tree -h                     # Print sizes in human readable format
tree -s                     # Print size of each file
tree -D                     # Print last modification date
```

## FILE FILTERING

```bash
tree --filelimit 15         # Don't descend dirs with >15 files
tree --dirsfirst            # List directories before files
tree -t                     # Sort by modification time
tree -r                     # Reverse sort order
tree --du                   # Print directory sizes
```

## OUTPUT FORMATS

```bash
tree -H baseHREF            # Generate HTML output
tree -X                     # Generate XML output
tree -J                     # Generate JSON output
tree -o filename            # Send output to filename
```

## DATA SCIENCE PROJECT EXAMPLES

```bash
# 1. Ignore Python cache and git files
tree -I '__pycache__|*.pyc|.git|.venv'

# 2. Show only code and config files
tree -P '*.py|*.ipynb|*.yml|*.yaml' -I '.git'

# 3. Show structure with file sizes, directories first
tree -L 3 --dirsfirst -h

# 4. Export project structure as JSON
tree -J -o project_structure.json
```
```

---

## find_grep.md

```markdown
----------------------------------------------------------------
| FIND/XARGS/GREP/SED/AWK CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## FIND - FILE DISCOVERY

```bash
find . -name "*.py"            # Find Python files
find . -type f -size +100M     # Find large files (>100MB)
find . -mtime -7               # Files modified in last 7 days
find . -name "*.log" -delete   # Find and delete log files
find . -type d -empty          # Find empty directories
find . -perm 777               # Find files with 777 permissions
find . -user $USER             # Find files owned by current user
```

## FIND WITH EXEC & XARGS

```bash
# Find Python files containing pandas import
find . -name "*.py" -exec grep -l "import pandas" {} \;
find . -name "*.py" | xargs grep -l "import pandas"

# Remove compiled Python files
find . -type f -name "*.pyc" | xargs rm

# Count lines in Python files
find . -name "*.py" | xargs wc -l

# Handle filenames with spaces
find . -name "*.py" -print0 | xargs -0 grep "TODO"
```

## GREP - PATTERN MATCHING

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

## SED - STREAM EDITOR

```bash
sed 's/old/new/g' file         # Replace all occurrences
sed -i 's/old/new/g' file      # In-place replacement
sed '5d' file                  # Delete line 5
sed '1,5d' file                # Delete lines 1-5
sed '/pattern/d' file          # Delete lines containing pattern
sed -n '10,20p' file           # Print lines 10-20
sed 's/^/  /' file             # Add 2 spaces to start of each line
sed '/pattern/a\new line' file # Add line after pattern match
```

## AWK - TEXT PROCESSING

```bash
awk '{print $1}' file          # Print first column
awk -F: '{print $1}' /etc/passwd # Use colon as delimiter
awk '$3 > 50' data.txt        # Print lines where column 3 > 50
awk '{sum += $1} END {print sum}' file # Sum first column
awk 'length > 80' file         # Print lines longer than 80 chars
awk '/pattern/ {print $2}' file # Print col 2 of lines with pattern
awk '{print NF, $0}' file     # Print number of fields per line
```

## DATA SCIENCE POWER COMBINATIONS

```bash
# 1. Find Python files using sklearn
find . -name "*.py" | xargs grep -l "sklearn" | head -10

# 2. Count lines in CSV files, sorted by size
find . -name "*.csv" -exec wc -l {} + | sort -n

# 3. Find TODO and FIXME comments in Python files
grep -r "TODO\|FIXME" --include="*.py" .

# 4. List all function definitions with filenames
find . -name "*.py" | xargs awk '/^def / {print FILENAME ": " $0}'

# 5. Extract class definitions (no comments)
sed -n '/class /,/def /p' *.py | grep -v "^#"
```
```

---

## cron.md

```markdown
----------------------------------------------------------------
| CRON CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## CRON BASICS

```bash
crontab -e                   # Edit current user's crontab
crontab -l                   # List current user's cron jobs
crontab -r                   # Remove current user's crontab
sudo crontab -u user -e      # Edit another user's crontab
sudo service crond restart   # Restart cron daemon
```

## CRON FORMAT

```
* * * * * command            # Min Hour Day Month DayOfWeek
┌───────────── minute (0-59)
│ ┌─────────── hour (0-23)
│ │ ┌───────── day of month (1-31)
│ │ │ ┌─────── month (1-12)
│ │ │ │ ┌───── day of week (0-6, Sunday=0)
│ │ │ │ │
* * * * *
```

## COMMON PATTERNS

```bash
0 0 * * *                   # Daily at midnight
0 */6 * * *                 # Every 6 hours
30 2 * * 1                  # Every Monday at 2:30 AM
0 9-17 * * 1-5              # Every hour 9-5, weekdays only
*/15 * * * *                # Every 15 minutes
0 0 1 * *                   # First day of every month
0 0 * * 0                   # Every Sunday at midnight
```

## SPECIAL STRINGS

```bash
@reboot                     # Run once at startup
@yearly                     # Run once a year (0 0 1 1 *)
@annually                   # Same as @yearly
@monthly                    # Run once a month (0 0 1 * *)
@weekly                     # Run once a week (0 0 * * 0)
@daily                      # Run once a day (0 0 * * *)
@midnight                   # Same as @daily
@hourly                     # Run once an hour (0 * * * *)
```

## DATA SCIENCE EXAMPLES

```bash
# Daily ETL pipeline at 2 AM
0 2 * * * /path/to/venv/bin/python /opt/etl/daily_pipeline.py

# Model training every Sunday at 3 AM
0 3 * * 0 /path/to/venv/bin/python /opt/ml/train_model.py

# Data backup every 6 hours
0 */6 * * * /opt/scripts/backup_data.sh

# Log rotation monthly
0 0 1 * * /usr/sbin/logrotate /etc/logrotate.conf
```

## CRON BEST PRACTICES

- Always use absolute paths for commands and files
- Set environment variables at the top of crontab
- Redirect output: > /dev/null 2>&1 or >> /var/log/cron.log
- Test scripts manually before adding to cron
- Use /var/log/cron for debugging cron issues
```

---

## git.md

```markdown
----------------------------------------------------------------
| GIT CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC OPERATIONS

```bash
git init                     # Initialize new repository
git clone url                # Clone remote repository
git status                   # Show working directory status
git add file                 # Stage specific file
git add .                    # Stage all changes
git commit -m "message"      # Commit staged changes
git commit -am "message"     # Stage and commit all changes
```

## BRANCHING & MERGING

```bash
git branch                   # List local branches
git branch -a                # List all branches (local + remote)
git branch feature-branch    # Create new branch
git checkout branch-name     # Switch to branch
git checkout -b new-branch   # Create and switch to new branch
git merge feature-branch     # Merge branch into current
git branch -d branch-name    # Delete local branch
```

## REMOTE OPERATIONS

```bash
git remote -v                # Show remote repositories
git fetch                    # Fetch changes from remote
git pull                     # Fetch and merge remote changes
git push                     # Push changes to remote
git push -u origin branch    # Push and set upstream
git push --force-with-lease  # Safer force push
```

## HISTORY & INSPECTION

```bash
git log                      # Show commit history
git log --oneline            # Compact commit history
git log --graph --oneline    # Visual branch history
git show commit-hash         # Show specific commit details
git diff                     # Show unstaged changes
git diff --staged            # Show staged changes
git blame file               # Show who changed each line
```

## UNDOING CHANGES

```bash
git reset HEAD file          # Unstage file
git checkout -- file         # Discard changes to file
git reset --soft HEAD~1      # Undo last commit, keep changes
git reset --hard HEAD~1      # Undo last commit, discard changes
git revert commit-hash       # Create new commit undoing changes
git stash                    # Temporarily save changes
git stash pop                # Apply and remove latest stash
```

## DATA SCIENCE WORKFLOW

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
```

---

## docker.md

```markdown
----------------------------------------------------------------
| DOCKER CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## CONTAINER MANAGEMENT

```bash
docker run image             # Run container from image
docker run -it image bash    # Run interactive container
docker run -d image          # Run container in background
docker run -p 8080:80 image  # Map port 8080 to container port 80
docker ps                    # List running containers
docker ps -a                 # List all containers
docker stop container-id     # Stop running container
docker rm container-id       # Remove container
```

## IMAGE MANAGEMENT

```bash
docker images                # List local images
docker build -t name:tag .   # Build image from Dockerfile
docker pull image:tag        # Download image from registry
docker push image:tag        # Upload image to registry
docker rmi image-id          # Remove image
docker history image         # Show image build history
```

## CONTAINER INTERACTION

```bash
docker exec -it container bash # Enter running container
docker logs container        # View container logs
docker logs -f container     # Follow container logs
docker cp file container:/path # Copy file to container
docker cp container:/path file # Copy file from container
```

## DOCKER COMPOSE

```bash
docker-compose up            # Start all services
docker-compose up -d         # Start services in background
docker-compose down          # Stop and remove services
docker-compose build         # Build all services
docker-compose logs service  # View service logs
docker-compose exec service bash # Enter service container
```

## SYSTEM CLEANUP

```bash
docker system prune          # Remove unused data
docker container prune       # Remove stopped containers
docker image prune           # Remove unused images
docker volume prune          # Remove unused volumes
docker system df             # Show docker disk usage
```

## DATA SCIENCE EXAMPLES

```bash
# Jupyter notebook container
docker run -p 8888:8888 -v $(pwd):/work jupyter/scipy-notebook

# Python environment with dependencies
docker run -it -v $(pwd):/app python:3.11 bash

# PostgreSQL for data storage
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=pwd postgres
```
```

---

## commitizen.md

```markdown
----------------------------------------------------------------
| COMMITIZEN CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## COMMIT OPERATIONS

```bash
cz commit                   # Interactive commit wizard
cz c                        # Short form of commit
cz commit --dry-run         # Preview commit message
cz commit --retry           # Retry last commit
```

## VERSIONING & CHANGELOG

```bash
cz bump                     # Auto bump version
cz bump --dry-run           # Preview version bump
cz bump --increment PATCH   # Bump patch version
cz bump --increment MINOR   # Bump minor version
cz bump --increment MAJOR   # Bump major version
cz changelog                # Generate changelog
```

## INFORMATION & SETUP

```bash
cz info                     # Show current config
cz example                  # Show commit examples
cz schema                   # Show commit schema
cz init                     # Initialize commitizen
cz --version                # Show version
```

## CONFIGURATION

```bash
cz --name cz_conventional_commits  # Set commit style
cz check --commit-msg-file    # Check commit message
cz check --rev-range          # Check commit range
```

## COMMON COMMIT TYPES

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
```

---

## regex.md

```markdown
----------------------------------------------------------------
| REGEX CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC PATTERNS

```regex
.                           # Match any single character
*                           # Match 0 or more of preceding
+                           # Match 1 or more of preceding
?                           # Match 0 or 1 of preceding
^                           # Start of line
$                           # End of line
\                           # Escape special characters
```

## CHARACTER CLASSES

```regex
[abc]                       # Match any of a, b, or c
[a-z]                       # Match any lowercase letter
[A-Z]                       # Match any uppercase letter
[0-9]                       # Match any digit
[^abc]                      # Match anything except a, b, or c
\d                          # Match any digit [0-9]
\w                          # Match word character [a-zA-Z0-9_]
\s                          # Match whitespace
```

## QUANTIFIERS

```regex
{n}                         # Exactly n occurrences
{n,}                        # n or more occurrences
{n,m}                       # Between n and m occurrences
*?                          # Non-greedy match (0 or more)
+?                          # Non-greedy match (1 or more)
??                          # Non-greedy match (0 or 1)
```

## GROUPS & ALTERNATION

```regex
(pattern)                   # Capture group
(?:pattern)                # Non-capturing group
pattern1|pattern2          # Match either pattern1 or pattern2
\1, \2, etc               # Reference captured groups
```

## LOOKAHEAD & LOOKBEHIND

```regex
(?=pattern)                # Positive lookahead
(?!pattern)                # Negative lookahead
(?<=pattern)               # Positive lookbehind
(?<!pattern)               # Negative lookbehind
```

## DATA SCIENCE EXAMPLES

```regex
# Email validation
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Extract numbers from text
\d+\.?\d*

# Match Python function definitions
def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(

# Extract URLs
https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*

# CSV field extraction
"([^"]*)"|([^,]+)
```
```

---

## curl_httpie.md

```markdown
----------------------------------------------------------------
| CURL/HTTPIE CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## CURL BASICS

```bash
curl url                     # Simple GET request
curl -X POST url             # POST request
curl -H "Header: value" url  # Add custom header
curl -d "data" url           # Send data in request body
curl -u user:pass url        # Basic authentication
curl -L url                  # Follow redirects
curl -o file url             # Save response to file
curl -I url                  # HEAD request (headers only)
```

## CURL ADVANCED

```bash
curl -X PUT -T file url      # Upload file with PUT
curl -F "file=@path" url     # Upload file via form
curl -b cookies.txt url       # Send cookies from file
curl -c cookies.txt url       # Save cookies to file
curl -w "%{http_code}" url   # Show only HTTP status code
curl --compressed url         # Request compressed response
curl -m 30 url                # 30 second timeout
```

## CURL JSON & APIS

```bash
# POST JSON data
curl -H "Content-Type: application/json" -d '{"key":"value"}' url

# Request JSON response
curl -H "Accept: application/json" url

# Bearer token authentication
curl -H "Authorization: Bearer token" url

# DELETE request
curl -X DELETE url
```

## HTTPIE BASICS

```bash
http GET url                 # Simple GET request
http POST url                # POST request
http url header:value        # Add custom header
http POST url key=value      # Send JSON data
http -a user:pass url        # Basic authentication
http --follow url            # Follow redirects
http --download url          # Download file
```

## HTTPIE ADVANCED

```bash
http PUT url < file          # Upload file content
http --form POST url file@path # Upload file via form
http --session=session url   # Use persistent session
http --json url              # Force JSON content type
http --timeout=30 url        # 30 second timeout
http --verify=no url         # Skip SSL verification
```

## API TESTING EXAMPLES

```bash
# Test REST API with curl
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"John","age":30}' \
     https://api.example.com/users

# Same with HTTPie
http POST api.example.com/users name=John age:=30

# Test with authentication
http GET api.example.com/data Authorization:"Bearer $TOKEN"
```
```

## uv.md

```markdown
----------------------------------------------------------------
| UV PYTHON CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## PROJECT MANAGEMENT

```bash
uv init                     # Initialize new project
uv init --app               # Initialize application
uv init --lib               # Initialize library
uv sync                     # Sync project dependencies
uv run                      # Run command in project env
uv run python script.py    # Run Python script
```

## PACKAGE MANAGEMENT

```bash
uv add package              # Add dependency
uv add --dev package        # Add dev dependency
uv add --optional extras    # Add optional dependency
uv remove package           # Remove dependency
uv lock                     # Update lock file
uv tree                     # Show dependency tree
```

## TESTING WITH PYTEST

```bash
uv add pytest --dev        # Add pytest as dev dependency
uv add pytest-cov --dev    # Add coverage support
uv add pytest-mock --dev   # Add mocking support
uv add pytest-xdist --dev  # Add parallel test execution
uv run pytest              # Run all tests
uv run pytest -v           # Run tests with verbose output
uv run pytest --cov        # Run tests with coverage
uv run pytest -x           # Stop on first failure
uv run pytest -k "test_name" # Run specific test pattern
uv run pytest tests/test_file.py # Run specific test file
uv run pytest --tb=short   # Short traceback format
```

## VIRTUAL ENVIRONMENTS

```bash
uv venv                     # Create virtual environment
uv venv --python 3.11      # Create with specific Python
uv venv .venv               # Create in specific directory
source .venv/bin/activate   # Activate environment (Unix)
.venv\Scripts\activate     # Activate environment (Windows)
```

## PACKAGE OPERATIONS

```bash
uv pip install package      # Install package (pip mode)
uv pip list                 # List installed packages
uv pip show package         # Show package info
uv pip freeze               # Export requirements
uv pip compile requirements.in # Compile requirements
```

## PYTHON VERSION MANAGEMENT

```bash
uv python list             # List available Python versions
uv python install 3.11     # Install Python version
uv python find              # Find Python installations
uv python pin 3.11         # Pin Python version for project
```

## PERFORMANCE & UTILITIES

```bash
uv cache clean              # Clear cache
uv cache dir                # Show cache directory
uv --version                # Show UV version
uv help                     # Show help
```

## QUICK START WORKFLOW

```bash
# 1. Initialize project
uv init my-project && cd my-project

# 2. Add dependencies
uv add requests

# 3. Add dev dependencies
uv add pytest --dev

# 4. Run application
uv run python main.py
```

## TESTING WORKFLOW

```bash
# 1. Add testing dependencies
uv add pytest pytest-cov --dev

# 2. Create tests directory with test_*.py files
mkdir tests && touch tests/test_main.py

# 3. Run tests with coverage
uv run pytest --cov=src --cov-report=html

# 4. Open coverage report
open htmlcov/index.html
```
```

---

## uv_pyproject.md

```markdown
----------------------------------------------------------------
| UV PYPROJECT CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## PROJECT STRUCTURE

```
pyproject.toml              # Main project configuration
uv.lock                     # Lockfile with exact versions
src/package_name/           # Source code directory
tests/                      # Test directory
README.md                   # Project documentation
```

## PYPROJECT.TOML SECTIONS

```toml
[project]                   # Basic project metadata
[project.dependencies]      # Runtime dependencies
[project.optional-dependencies] # Dev/optional deps
[build-system]              # Build configuration
[tool.uv]                   # UV-specific settings
[tool.pytest.ini_options]   # Pytest configuration
```

## DEPENDENCY GROUPS

```bash
uv add pandas               # Add to main dependencies
uv add --dev pytest         # Add to dev dependencies
uv add --group docs sphinx  # Add to docs group
uv add --optional ml torch  # Add to optional ML group
uv sync --group docs        # Install docs dependencies
uv sync --all-groups        # Install all dependency groups
```

## VERSION CONSTRAINTS

```bash
uv add "pandas>=1.5,<3.0"  # Version range constraint
uv add "numpy~=1.24.0"     # Compatible release (>=1.24.0, <1.25.0)
uv add "requests==2.31.0"  # Exact version pin
uv add "scipy>=1.10"       # Minimum version constraint
```

## WORKSPACE MANAGEMENT

```toml
[tool.uv.workspace]         # Define workspace root
members = ["packages/*"]   # Workspace member packages
```

```bash
uv sync --workspace          # Sync entire workspace
uv run --package pkg script  # Run script in specific package
```

## EXAMPLE PYPROJECT.TOML

```toml
[project]
name = "my-ml-project"
version = "0.1.0"
description = "Machine learning project using UV"
authors = [{name = "Your Name", email = "you@example.com"}]
dependencies = [
    "pandas>=1.5",
    "scikit-learn>=1.3",
    "numpy>=1.24"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "ruff>=0.1.0",
    "mypy>=1.0"
]
ml = [
    "torch>=2.0",
    "tensorflow>=2.13"
]
viz = [
    "matplotlib>=3.7",
    "seaborn>=0.12",
    "plotly>=5.15"
]

[tool.uv]
dev-dependencies = [
    "pytest-cov>=4.0",
    "pytest-mock>=3.10"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = "--cov=src --cov-report=html --cov-report=term"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.black]
line-length = 88
target-version = ['py311']

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
```

---

## pytest.md

```markdown
----------------------------------------------------------------
| PYTEST CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC COMMANDS

```bash
pytest                      # Run all tests
pytest test_file.py        # Run specific test file
pytest -k "test_name"     # Run tests matching pattern
pytest -v                  # Verbose output
pytest -s                  # Don't capture stdout
pytest -x                  # Stop on first failure
pytest --lf                # Run last failed tests only
pytest --tb=short          # Short traceback format
```

## TEST DISCOVERY & SELECTION

```bash
pytest tests/unit/         # Run tests in specific directory
pytest -m "slow"          # Run tests marked as 'slow'
pytest -m "not slow"      # Skip tests marked as 'slow'
pytest --collect-only      # Show which tests would run
pytest -k "test_api and not slow" # Complex test selection
```

## COVERAGE & REPORTING

```bash
pytest --cov               # Basic coverage report
pytest --cov=src           # Coverage for src directory
pytest --cov-report=html   # Generate HTML coverage report
pytest --cov-report=term-missing # Show missing lines
pytest --cov-fail-under=80 # Fail if coverage < 80%
pytest --cov-branch        # Include branch coverage
```

## FIXTURES & MARKERS

```python
@pytest.fixture            # Define reusable test data
def sample_data():
    return {"key": "value"}

@pytest.mark.parametrize   # Run test with multiple inputs
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6)
])
def test_double(input, expected):
    assert double(input) == expected

@pytest.mark.skip          # Skip test unconditionally
@pytest.mark.skipif        # Skip test conditionally
@pytest.mark.xfail         # Expected to fail
@pytest.mark.slow          # Custom marker for slow tests
```

## PARALLEL EXECUTION

```bash
pytest -n auto             # Auto-detect CPU cores
pytest -n 4                # Run with 4 processes
pytest --dist loadscope    # Distribute by test scope
pytest --dist loadfile     # Distribute by test file
```

## DATA SCIENCE TEST EXAMPLES

```python
# Test DataFrame operations
def test_data_cleaning(sample_df):
    result = clean_data(sample_df)
    assert result.isna().sum().sum() == 0
    assert len(result) > 0

# Test model performance
@pytest.mark.parametrize("model", ["lr", "rf", "xgb"])
def test_model_accuracy(model, test_data):
    score = evaluate_model(model, test_data)
    assert score > 0.8

# Test data pipeline
def test_feature_engineering():
    raw_data = load_raw_data()
    features = engineer_features(raw_data)
    assert features.shape[1] > raw_data.shape[1]
    assert not features.isnull().any().any()

# Test API endpoints
def test_prediction_endpoint(client):
    response = client.post('/predict', 
                         json={'features': [1.0, 2.0, 3.0]})
    assert response.status_code == 200
    assert 'prediction' in response.json()
```

## PYTEST CONFIGURATION

```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --cov=src
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80

markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```
```

---

## pandas.md

```markdown
----------------------------------------------------------------
| PANDAS CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## DATA LOADING & SAVING

```python
import pandas as pd

# Loading data
pd.read_csv('file.csv')     # Read CSV file
pd.read_excel('file.xlsx')  # Read Excel file
pd.read_json('file.json')   # Read JSON file
pd.read_sql(query, conn)    # Read from SQL database
pd.read_parquet('file.parquet') # Read Parquet file

# Saving data
df.to_csv('file.csv', index=False)       # Save as CSV
df.to_excel('file.xlsx', index=False)    # Save as Excel
df.to_json('file.json')     # Save as JSON
df.to_sql('table', conn)    # Save to SQL database
df.to_parquet('file.parquet') # Save as Parquet
```

## DATA EXPLORATION

```python
df.head()                   # First 5 rows
df.tail()                   # Last 5 rows
df.info()                   # Data types and null counts
df.describe()               # Statistical summary
df.shape                    # Dimensions (rows, columns)
df.columns                  # Column names
df.dtypes                   # Data types of columns
df.isnull().sum()           # Count missing values
df.value_counts()           # Count unique values in Series
df.nunique()                # Count unique values per column
```

## DATA SELECTION & FILTERING

```python
# Column selection
df['column']                # Select single column
df[['col1', 'col2']]        # Select multiple columns

# Row selection
df.loc[row_index, 'column'] # Label-based selection
df.iloc[0:5, 1:3]           # Position-based selection
df.head(10)                 # First 10 rows

# Filtering
df[df['column'] > 5]        # Filter rows by condition
df.query('column > 5')      # Query-style filtering
df[df['col'].isin(['a', 'b'])] # Filter by values in list
df.sample(n=100)            # Random sample of rows
df.sample(frac=0.1)         # Random 10% sample
```

## DATA CLEANING

```python
# Missing values
df.dropna()                 # Remove rows with missing values
df.dropna(subset=['col'])   # Remove rows with missing values in specific column
df.fillna(value)            # Fill missing values with value
df.fillna(method='ffill')   # Forward fill
df.fillna(method='bfill')   # Backward fill
df['col'].fillna(df['col'].mean()) # Fill with mean

# Duplicates and data issues
df.drop_duplicates()        # Remove duplicate rows
df.drop('column', axis=1)   # Drop column
df.rename(columns={'old': 'new'}) # Rename columns
df['col'].astype('int')     # Change data type
df.replace(old_value, new_value) # Replace values
```

## GROUPING & AGGREGATION

```python
# Basic grouping
df.groupby('column').mean() # Group by and calculate mean
df.groupby(['col1', 'col2']).sum() # Group by multiple columns

# Multiple aggregations
df.groupby('col').agg({
    'col2': 'sum',
    'col3': ['mean', 'std'],
    'col4': 'count'
})

# Transform and apply
df.groupby('col')['value'].transform('mean') # Add group mean to each row
df.groupby('col').apply(custom_function)     # Apply custom function to groups

# Pivot tables
df.pivot_table(
    values='sales',
    index='product',
    columns='region',
    aggfunc='sum'
)
```

## MERGING & JOINING

```python
# Concatenating
pd.concat([df1, df2])       # Concatenate DataFrames vertically
pd.concat([df1, df2], axis=1) # Concatenate horizontally

# Merging
df1.merge(df2, on='key')    # Inner join on key
df1.merge(df2, how='left')  # Left join
df1.merge(df2, how='outer') # Outer join
df1.merge(df2, left_on='col1', right_on='col2') # Different column names

# Joining (index-based)
df1.join(df2)               # Join on index
```

## DATETIME OPERATIONS

```python
# Convert to datetime
pd.to_datetime(df['date'])  # Convert string to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract datetime components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek

# Resampling time series
df.set_index('date').resample('D').mean()  # Daily averages
df.set_index('date').resample('M').sum()   # Monthly sums
```

## COMMON ML PREPROCESSING

```python
# Handle missing values
df['column'].fillna(df['column'].median(), inplace=True)

# Create dummy variables
pd.get_dummies(df['category'], prefix='cat')

# Feature scaling (normalize)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['col1', 'col2']] = scaler.fit_transform(df[['col1', 'col2']])

# Or manually
df['normalized'] = (df['column'] - df['column'].mean()) / df['column'].std()

# Binning continuous variables
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100], 
                        labels=['child', 'young', 'middle', 'senior'])

# Apply custom functions
df['new_col'] = df['col'].apply(lambda x: x * 2)
df['new_col'] = df.apply(lambda row: row['col1'] + row['col2'], axis=1)
```
```

---

## flask.md

```markdown
----------------------------------------------------------------
| FLASK CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC SETUP

```python
from flask import Flask

app = Flask(__name__)       # Create Flask app

@app.route('/')             # Define route decorator
def home():
    return 'Hello, World!'  # Route function

if __name__ == '__main__':
    app.run(debug=True)     # Run development server
    # app.run(host='0.0.0.0', port=5000) # Custom host/port
```

## ROUTING & HTTP METHODS

```python
@app.route('/path')         # GET route (default)
def get_data():
    return 'GET request'

@app.route('/path', methods=['POST'])  # POST route
def post_data():
    return 'POST request'

@app.route('/user/<name>')  # Dynamic route with parameter
def user_profile(name):
    return f'User: {name}'

@app.route('/post/<int:id>') # Integer parameter
def show_post(id):
    return f'Post ID: {id}'

@app.route('/api', methods=['GET', 'POST']) # Multiple methods
def api_endpoint():
    if request.method == 'POST':
        return 'POST data received'
    return 'GET request'
```

## REQUEST HANDLING

```python
from flask import request

@app.route('/form', methods=['POST'])
def handle_form():
    # Form data
    username = request.form['username']
    password = request.form['password']
    
    # URL parameters
    page = request.args.get('page', 1, type=int)
    
    # JSON data
    data = request.json
    
    # Uploaded files
    file = request.files['file']
    
    # Request method
    method = request.method
    
    return f'Received: {username}'
```

## RESPONSES & TEMPLATES

```python
from flask import render_template, jsonify, redirect, url_for

@app.route('/page')
def show_page():
    # Render HTML template
    return render_template('page.html', title='My Page')

@app.route('/api/data')
def api_data():
    # Return JSON response
    return jsonify({'key': 'value', 'status': 'success'})

@app.route('/redirect')
def redirect_example():
    # Redirect to another route
    return redirect(url_for('home'))

@app.route('/custom')
def custom_response():
    # Custom response with status code
    return 'Custom response', 201
```

## ERROR HANDLING

```python
@app.errorhandler(404)
def not_found(error):
    return 'Page not found', 404

@app.errorhandler(500)
def server_error(error):
    return 'Internal server error', 500

@app.route('/protected')
def protected_route():
    try:
        # Some operation that might fail
        result = risky_operation()
        return jsonify({'result': result})
    except Exception as e:
        app.logger.error(f'Error in protected route: {str(e)}')
        return jsonify({'error': 'Something went wrong'}), 500
```

## ML API EXAMPLE

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        features = data['features']
        
        # Convert to numpy array
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0].max()
        
        return jsonify({
            'prediction': float(prediction),
            'probability': float(probability),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)
```

## TESTING FLASK APIS

```bash
# Test with curl
curl -X POST -H "Content-Type: application/json" \
     -d '{"features":[1.0, 2.0, 3.0, 4.0]}' \
     http://localhost:5000/predict

# Test with HTTPie
http POST localhost:5000/predict features:='[1.0, 2.0, 3.0, 4.0]'
```

## FLASK CONFIGURATION

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    
class ProductionConfig(Config):
    DEBUG = False
    
app.config.from_object(Config)
```
```

---

## fastapi.md

```markdown
----------------------------------------------------------------
| FASTAPI CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## BASIC SETUP

```python
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")               # GET route decorator
async def root():
    return {"message": "Hello World"}

# Run with: uvicorn main:app --reload
```

## HTTP METHODS & ROUTES

```python
@app.get("/items")          # GET endpoint
async def read_items():
    return {"items": []}

@app.post("/items")         # POST endpoint
async def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")     # PUT endpoint with path param
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")  # DELETE endpoint
async def delete_item(item_id: int):
    return {"deleted": item_id}

@app.patch("/items/{item_id}")   # PATCH endpoint
async def patch_item(item_id: int, updates: dict):
    return {"item_id": item_id, "updates": updates}
```

## PATH & QUERY PARAMETERS

```python
from typing import Optional

@app.get("/items/{item_id}") # Path parameter
async def read_item(item_id: int):  # Type hint for validation
    return {"item_id": item_id}

# Query parameters
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Optional query parameters
@app.get("/search/")
async def search_items(q: Optional[str] = None, category: str = "all"):
    return {"query": q, "category": category}
```

## REQUEST & RESPONSE MODELS

```python
from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):      # Define request model
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemResponse(BaseModel): # Define response model
    id: int
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
async def create_item(item: Item):  # Use model for validation
    # Process item
    return ItemResponse(id=1, name=item.name, price=item.price)

@app.get("/items/", response_model=List[ItemResponse])
async def read_items():
    return [ItemResponse(id=1, name="Item 1", price=10.0)]
```

## DEPENDENCY INJECTION

```python
from fastapi import Depends

def get_db():               # Dependency function
    db = create_database_connection()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
async def read_items(db = Depends(get_db)):  # Inject dependency
    return fetch_items_from_db(db)

# Nested dependencies
def get_current_user(token: str = Depends(get_token)):
    return verify_token(token)

@app.get("/protected/")
async def protected_route(user = Depends(get_current_user)):
    return {"user": user}
```

## ASYNC & BACKGROUND TASKS

```python
import asyncio
from fastapi import BackgroundTasks

async def read_items():     # Async endpoint
    data = await fetch_data_async()
    return data

def send_email(email: str): # Background function
    # Send email logic
    print(f"Sending email to {email}")

@app.post("/send-email/")
async def send_email_endpoint(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email)
    return {"message": "Email will be sent"}
```

## ML API EXAMPLE WITH FASTAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib

app = FastAPI(title="ML Prediction API", version="1.0.0")

# Load model at startup
model = joblib.load("model.pkl")

class PredictionRequest(BaseModel):
    features: List[float]

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float
    model_version: str

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        # Convert features to numpy array
        features_array = np.array(request.features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        confidence = model.predict_proba(features_array)[0].max()
        
        return PredictionResponse(
            prediction=float(prediction),
            confidence=float(confidence),
            model_version="1.0.0"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.get("/model/info")
async def model_info():
    return {
        "model_type": type(model).__name__,
        "features": getattr(model, 'n_features_in_', 'unknown'),
        "version": "1.0.0"
    }

# Auto-generated docs available at: http://localhost:8000/docs
# Alternative docs at: http://localhost:8000/redoc
```

## ERROR HANDLING

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return {"error": "Invalid value", "detail": str(exc)}
```

## MIDDLEWARE & CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```
```

---

## django.md

```markdown
----------------------------------------------------------------
| DJANGO CHEAT SHEET |
| v1 |
----------------------------------------------------------------

## PROJECT SETUP

```bash
# Install Django
pip install django djangorestframework

# Create new project
django-admin startproject myproject
cd myproject

# Create new app
python manage.py startapp myapp

# Run development server
python manage.py runserver

# Database operations
python manage.py makemigrations  # Create migrations
python manage.py migrate         # Apply migrations
python manage.py createsuperuser # Create admin user
```

## MODELS & DATABASE

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='datasets/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    algorithm = models.CharField(max_length=50)
    parameters = models.JSONField(default=dict)
    accuracy = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

## VIEWS & URLS

```python
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dataset, Experiment
import json

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets/list.html', {'datasets': datasets})

def dataset_detail(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    experiments = Experiment.objects.filter(dataset=dataset)
    return render(request, 'datasets/detail.html', {
        'dataset': dataset,
        'experiments': experiments
    })

@csrf_exempt
def api_predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        features = data.get('features', [])
        
        # Your ML prediction logic here
        prediction = make_prediction(features)
        
        return JsonResponse({
            'prediction': prediction,
            'status': 'success'
        })
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('dataset/<int:pk>/', views.dataset_detail, name='dataset_detail'),
    path('api/predict/', views.api_predict, name='api_predict'),
]
```

## DJANGO REST FRAMEWORK

```python
# serializers.py
from rest_framework import serializers
from .models import Dataset, Experiment

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ExperimentSerializer(serializers.ModelSerializer):
    dataset_name = serializers.CharField(source='dataset.name', read_only=True)
    
    class Meta:
        model = Experiment
        fields = '__all__'
        read_only_fields = ('created_at',)

# API views using DRF
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    
    @action(detail=True, methods=['post'])
    def run_experiment(self, request, pk=None):
        dataset = self.get_object()
        algorithm = request.data.get('algorithm')
        parameters = request.data.get('parameters', {})
        
        # Run ML experiment
        result = run_ml_experiment(dataset, algorithm, parameters)
        
        # Create experiment record
        experiment = Experiment.objects.create(
            name=f"{algorithm}_experiment",
            dataset=dataset,
            algorithm=algorithm,
            parameters=parameters,
            accuracy=result['accuracy']
        )
        
        return Response({
            'experiment_id': experiment.id,
            'accuracy': result['accuracy'],
            'status': 'completed'
        })

# urls.py for API
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'datasets', views.DatasetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
```

## ADMIN INTERFACE

```python
# admin.py
from django.contrib import admin
from .models import Dataset, Experiment

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_at', 'file']
    list_filter = ['created_at', 'owner']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ['name', 'dataset', 'algorithm', 'accuracy', 'created_at']
    list_filter = ['algorithm', 'created_at']
    search_fields = ['name', 'dataset__name']
    readonly_fields = ['created_at']
```

## SETTINGS CONFIGURATION

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'myapp',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or sqlite3
        'NAME': os.environ.get('DB_NAME', 'myproject'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## ML PROJECT STRUCTURE

```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ml_api/              # ML API app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ml_utils.py      # ML helper functions
├── datasets/            # Dataset management app
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── models/              # ML models storage
│   └── trained_models/
├── static/              # CSS, JS files
├── media/               # Uploaded files
├── templates/           # HTML templates
├── requirements.txt     # Dependencies
└── manage.py
```

## USEFUL MANAGEMENT COMMANDS

```bash
# Database operations
python manage.py dbshell            # Database shell
python manage.py loaddata fixture   # Load test data
python manage.py dumpdata app       # Export data

# Development
python manage.py shell              # Django shell
python manage.py collectstatic      # Collect static files
python manage.py test               # Run tests

# Custom management command
python manage.py train_model --dataset=1 --algorithm=rf
```
```

---

## econometric_terms.md

```markdown
----------------------------------------------------------------
| ECONOMETRIC TERMS (SIMPLE ENGLISH) |
| v1 |
----------------------------------------------------------------

## BIAS & IDENTIFICATION

**Selection Bias**
When your sample isn't representative of the population you want to study. Like surveying only smartphone users about technology preferences.

**Omitted Variable Bias**
Missing important factors in your model that affect both your outcome and predictor. Like studying salary vs education while ignoring work experience.

**Survivorship Bias**
Only looking at 'winners' who survived some process. Like analyzing successful startups while ignoring all the failed ones.

**Confirmation Bias**
Finding evidence that supports what you already believe. Cherry-picking data that confirms your hypothesis.

**Endogeneity**
When X affects Y, but Y also affects X. Hard to tell which direction causation flows. Does police presence reduce crime, or does crime increase police presence?

**Reverse Causality**
Getting cause and effect backwards. Thinking A causes B when actually B causes A.

## CENSORSHIP & MISSING DATA

**Censoring**
Data is cut off at some limit. Like a survey asking income with the top option being ">$100k" - you know high earners exist but not their exact income.

**Truncation**
Missing data below or above a threshold entirely. Like only having data on students who scored above 50% - the low performers aren't in your dataset at all.

**Attrition**
People dropping out of a study over time. In a 5-year health study, some participants might move away or lose interest.

**Missing at Random (MAR)**
Missing data depends on variables you can observe. Wealthy people might be less likely to report income, but you can see their neighborhood.

**Missing Not at Random (MNAR)**
Missing data depends on unobserved factors. People with depression might be less likely to complete mental health surveys.

**Listwise Deletion**
Throwing out entire rows with any missing data. Quick but potentially wasteful solution.

## CAUSAL INFERENCE

**Treatment Effect**
The impact of an intervention or policy. How much does a job training program increase wages?

**Control Group**
The 'no treatment' comparison group. In a drug trial, people who get a placebo instead of the real medicine.

**Randomized Control Trial (RCT)**
Gold standard - randomly assign who gets treatment. Like flipping a coin to decide who gets the job training program.

**Natural Experiment**
Random-like variation from the real world. Like using a lottery to determine who gets college scholarships.

**Instrumental Variable**
A tool to isolate causal effects when you can't run an experiment. Like using rainfall to study how agricultural income affects education (rainfall affects income but not education directly).

**Difference-in-Differences**
Compare changes over time between groups. How did minimum wage increases affect employment in states that raised it vs. states that didn't?

**Regression Discontinuity**
Using sharp cutoffs to create quasi-experiments. Study effects of a program by comparing people just above vs. just below the eligibility threshold.

## MODEL ASSUMPTIONS & PROBLEMS

**Heteroskedasticity**
Error variance changes across observations. Prediction errors might be larger for expensive houses than cheap ones.

**Autocorrelation**
Errors are correlated over time. If you underpredict sales today, you're likely to underpredict tomorrow too.

**Multicollinearity**
Predictor variables are highly correlated with each other. Makes it hard to separate their individual effects.

**Specification Error**
Wrong functional form or missing variables. Using a linear model when the relationship is actually curved.

**Overfitting**
Model is too complex and memorizes noise rather than learning patterns. Performs great on training data but terrible on new data.

**Underfitting**
Model is too simple and misses important patterns. Using a straight line to fit data that clearly curves.

## STATISTICAL CONCEPTS

**P-value**
Probability of seeing your results if there really is no effect. Low p-value means your result is unlikely to be due to random chance.

**Confidence Interval**
Range of plausible values for your parameter. "We're 95% confident the true effect is between 2 and 8."

**Standard Error**
Measure of uncertainty in your estimate. Smaller standard error means more precise estimate.

**Type I Error (False Positive)**
Finding an effect that isn't really there. Like thinking a coin is biased when it's actually fair.

**Type II Error (False Negative)**
Missing a real effect. Like thinking a coin is fair when it's actually biased.

**Power**
Ability to detect true effects when they exist. Higher power means less likely to miss real effects.

**Effect Size**
Magnitude of the relationship. Not just "is there an effect?" but "how big is the effect?"

## PANEL DATA CONCEPTS

**Fixed Effects**
Control for time-invariant differences between units. Each person/company has their own baseline level.

**Random Effects**
Assume individual differences are random draws from a population. More efficient if assumptions hold.

**Cross-sectional**
Data at one point in time. Like a snapshot of all companies in 2023.

**Time Series**
Data over time for one unit. Like Apple's stock price from 2020-2024.

**Panel Data**
Multiple units observed over time. Stock prices for all S&P 500 companies from 2020-2024.

**Balanced Panel**
All units observed for all time periods. No missing data.

**Unbalanced Panel**
Some units missing in some periods. Companies might go out of business or IPO during your study period.

## DATA SCIENCE APPLICATIONS

**A/B Testing**
Online version of randomized experiments. Show version A to half your users, version B to the other half.

**Cohort Analysis**
Track groups over time. How do users who signed up in January behave differently from those who signed up in June?

**Propensity Score Matching**
Match similar units for causal inference. Find non-participants who look just like program participants.

**Synthetic Control**
Create an artificial control group by combining multiple similar units. If California passes a law, create "synthetic California" from other states.

**Regression Adjustment**
Control for confounders statistically. Include other variables that might affect both treatment assignment and outcomes.

**Mediation Analysis**
How X affects Y through intermediate variable Z. Does education increase income directly or by improving job skills?

**Moderation/Interaction**
When the effect of X on Y depends on Z. Maybe job training works better for younger people than older people.

## PRACTICAL EXAMPLES

**Selection Bias Example**
Studying smartphone apps by only surveying people who downloaded your app from the App Store.

**Omitted Variable Example**
Looking at ice cream sales and drowning deaths (both caused by hot weather, which you didn't measure).

**Endogeneity Example**
Do more hospitals cause more deaths, or do more deaths cause more hospitals to be built?

**Censoring Example**
Survey asking "How many hours do you work per week?" with maximum option "60+ hours."

**Natural Experiment Example**
Vietnam War draft lottery - random birthdays determined who got drafted, letting you study effects of military service.

**Instrumental Variable Example**
Using distance to college as an instrument for education (affects education but not wages directly).
```
```