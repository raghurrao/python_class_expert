# Day 23: Code Coverage & Test Analytics (`pytest-cov`)

How do you know if your test suite is thorough? Code Coverage measures what percentage of your source code is executed when your tests run. Pytest integrates with the Python coverage engine using the **`pytest-cov`** plugin.

---

## 1. Running Coverage Analysis
To check the coverage of a module, run:
```bash
pytest --cov=my_module
```
This prints a terminal table showing:
* **Stmts**: Total statements in the code.
* **Miss**: Statements not executed during the tests.
* **Cover**: Coverage percentage.

---

## 2. Locating Untested Lines (`term-missing`)
To find the exact line numbers that were skipped, add the `--cov-report=term-missing` flag:
```bash
pytest --cov=my_module --cov-report=term-missing
```
Under the `Missing` column, it will print line ranges (e.g. `23-25, 45`) that were never run. You should write test cases targeting those exact branches!

---

## 3. Interactive Visual Reports (HTML)
Checking terminal text can be tedious. You can generate an interactive HTML dashboard:
```bash
pytest --cov=my_module --cov-report=html
```
This creates an `htmlcov/` folder in your workspace. Open `htmlcov/index.html` in your browser. It highlights executed lines in green and missed lines in red!

---

## 4. Enforcing Coverage Gates (`--cov-fail-under`)
In professional settings, teams enforce a minimum coverage threshold (e.g. 90%). If a commit drops coverage below this, the build fails.
You can configure this in your command line:
```bash
pytest --cov=my_module --cov-fail-under=90
```
If coverage is 89%, pytest exits with code 1 and fails the run, even if all tests passed!

### Configuring in `pytest.ini`:
```ini
[pytest]
addopts = --cov=day6_validator --cov-fail-under=90 --cov-report=term-missing
```
Now, simply running `pytest` will automatically trigger coverage analysis, check for 90% threshold, and list missing lines.
