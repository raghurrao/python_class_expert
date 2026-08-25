# Days 28-30: CI/CD Pipeline Integration & Best Practices

Congratulations! You have completed all coding assignments and the capstone project. In these final days, we focus on operationalizing your test suite by integrating it into a **Continuous Integration (CI)** pipeline and establishing professional testing style guides.

---

## 1. Integrating Pytest into GitHub Actions
To run your test suite automatically on every `git push` or pull request, create a file named `.github/workflows/test.yml` in your repository:

```yaml
name: Python Test Suite

on:
  push:
    branches: [ main, dev ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip' # cache dependencies

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-asyncio pytest-cov pytest-xdist requests

    - name: Run Pytest Suite
      run: |
        pytest --cov=. --cov-report=xml

    - name: Upload Coverage to Codecov (Optional)
      uses: codecov/codecov-action@v4
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
        file: ./coverage.xml
```

---

## 2. Integrating Pytest into GitLab CI
If your team uses GitLab, add the following configuration in a file named `.gitlab-ci.yml` in your project root:

```yaml
stages:
  - test

run_tests:
  stage: test
  image: python:3.11-slim
  before_script:
    - pip install --upgrade pip
    - pip install pytest pytest-asyncio pytest-cov pytest-xdist requests
  script:
    - pytest --cov=. --cov-report=term-missing --cov-fail-under=90
```

---

## 3. Formatting with Pre-Commit Hooks
To ensure developers format code and run styling checks before committing code locally, create a file named `.pre-commit-config.yaml` in your project root:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  # Enforce Python formatting (Black)
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3

  # Enforce Import Sorting (isort)
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  # Enforce Linting (Flake8)
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100]
```

To initialize these hooks in your git repository:
```bash
pip install pre-commit
pre-commit install
```

---

## 4. Professional Pytest Style Guide

### A. Keep Tests Focused
Each test function should test **one specific logical behavior**. Do not write a single test that asserts registration, checkout, payment, and receipts in a sequence. If the payment step fails, you won't know if the receipts step was also broken.

### B. Use AAA Pattern (Arrange, Act, Assert)
1. **Arrange**: Set up fixtures, inputs, and mocks.
2. **Act**: Call the function/method being tested.
3. **Assert**: Verify outputs, state changes, or database entries.

```python
def test_item_creation():
    # 1. Arrange
    price = 19.99
    
    # 2. Act
    item = Item("Notebook", price)
    
    # 3. Assert
    assert item.name == "Notebook"
    assert item.price == price
```

### C. Never Import from `conftest.py`
Fixtures defined in `conftest.py` are loaded dynamically by pytest. Explicitly importing from `conftest` is an anti-pattern and can cause dependency cycle errors.

### D. Avoid Shared Global State
Tests run in parallel inside CI. Never write assertions that depend on global variables mutable by other tests. Use fixtures with `yield` teardowns to reset states cleanly.

---

## 🎓 Next Steps
You have completed the entire Pytest Expert program! 
Here is your final checklist:
1. Complete assignments Day 1 to Day 27.
2. Run each verification script using `.venv\Scripts\python pytest_expert/verify_dayX.py`.
3. Read the review guides at Day 7, Day 14, and Day 21.

You are now equipped with the testing patterns used at top technology firms. Happy testing!
