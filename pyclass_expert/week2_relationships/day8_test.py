# Day 8 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day8_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.day8_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day8_assignment.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Day 8 Tests...\n")

# 1. Verification of Send Methods
def test_send_methods():
    assert hasattr(assignment, 'SmsSender'), "SmsSender missing"
    assert hasattr(assignment, 'EmailSender'), "EmailSender missing"
    assert hasattr(assignment, 'SlackSender'), "SlackSender missing"
    
    sms = assignment.SmsSender()
    email = assignment.EmailSender()
    slack = assignment.SlackSender()
    
    # Assert they do not share inheritance
    assert not isinstance(sms, assignment.EmailSender)
    assert not isinstance(email, assignment.SlackSender)
    
    assert sms.send("Alert", "123") == "SMS to 123: Alert"
    assert email.send("Alert", "a@b.com") == "Email to a@b.com: Alert"
    assert slack.send("Alert", "#dev") == "Slack to #dev: Alert"

run_test("Sender channels independent send implementations", test_send_methods)

# 2. Polymorphic Dispatcher Verification
def test_dispatcher():
    assert hasattr(assignment, 'NotificationDispatcher'), "NotificationDispatcher missing"
    
    sms_sender = assignment.SmsSender()
    email_sender = assignment.EmailSender()
    
    disp1 = assignment.NotificationDispatcher(sms_sender)
    disp2 = assignment.NotificationDispatcher(email_sender)
    
    assert disp1.dispatch("Hello", "555-0199") == "SMS to 555-0199: Hello"
    assert disp2.dispatch("Hello", "test@test.com") == "Email to test@test.com: Hello"
    
    # Assert Duck typing with a completely custom mock object
    class MockDuck:
        def send(self, msg, rec):
            return f"Mocked {msg} to {rec}"
            
    mock_disp = assignment.NotificationDispatcher(MockDuck())
    assert mock_disp.dispatch("Hello", "World") == "Mocked Hello to World", "Dispatcher did not correctly use duck typing!"

run_test("Dispatcher client polymorphic behavior (Duck Typing)", test_dispatcher)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 8 assignments.")
    print(f"Proceed to Day 9 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day8_assignment.py")
