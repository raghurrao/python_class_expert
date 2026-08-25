# Day 6: Week 1 Integration Assignment

Today is your first weekly milestone! We will consolidate everything you have learned this week into a single, comprehensive testing project. You will test a utility class called `DataValidator` that processes user signup inputs.

---

## The Challenge: Testing `DataValidator`
You are provided with a package containing `day6_validator.py`. It has methods to validate:
1. **Usernames** (must be alphanumeric, 3 to 20 characters).
2. **Emails** (must contain '@' and at least one '.').
3. **Passwords** (must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number).

Your job is to write a complete test suite inside `test_day6_assignment.py` following these specifications:

### 1. Test Organization
* Group all validation tests inside a class named `TestDataValidator`.

### 2. Exception & Output Verification
* Test normal cases (assert returning `True`).
* Test invalid types (assert raising `TypeError` and checking the message).
* Test invalid values (assert raising `ValueError` and checking specific error messages).

### 3. Custom Markers & Configuration
* Decorate username/email validation tests with your custom `@pytest.mark.fast` marker.
* Decorate password validation tests with a new custom `@pytest.mark.security` marker.
* Update your `pytest.ini` file to register this new `security` marker.

---

## Commands to Verify
Once you've written your test suite, verify it using:
```powershell
.venv\Scripts\python pytest_expert/verify_day6.py
```
This will run mutation tests against your test suite. Your test suite must catch all validation bugs in our mutated code to succeed!
