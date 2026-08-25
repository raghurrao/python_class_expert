# Day 26: Parallelization, Speed & Profiling (`pytest-xdist`)

In large-scale software, the test suite can take minutes or even hours to run. This slows down the deployment cycle. Today, we will learn how to profile slow tests and run your test suites in parallel using **`pytest-xdist`**.

---

## 1. Running Tests in Parallel (`-n`)
The `pytest-xdist` plugin allows you to distribute your test runs across multiple CPU cores. Each core runs a separate worker process:

* Run tests using 4 workers:
  ```bash
  pytest -n 4
  ```
* Run tests automatically matching the number of logical CPUs on your machine:
  ```bash
  pytest -n auto
  ```

---

## 2. Caveats of Parallel Test Execution
Running tests in parallel introduces concurrent execution, which can cause tests to fail if they are not isolated:

1. **Shared Files**: If two tests write to `data.txt` in the same directory, they will overwrite each other's data (race condition). Using `tmp_path` solves this, as it generates a unique directory for each worker!
2. **Shared Databases**: If tests write to the same database tables concurrently, row counts and constraints will bleed across tests.
3. **Execution Order**: Tests run out of order. Never write a test that expects another test to have run before it.

---

## 3. Profiling Slow Tests (`--durations`)
Before parallelizing, you should identify which tests are taking the most time:
```bash
pytest --durations=5
```
This runs the suite and prints a list of the **top 5 slowest tests** (including setup, execution call, and teardown). This helps you target code optimizations, database indexing, or mocking slow calls.
