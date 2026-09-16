import os
import sys
import subprocess
import glob

def run_all_tests():
    """
    Recursively scans the workspace for files ending in _test.py and runs them 
    using the active Python interpreter.
    """
    workspace_root = os.path.dirname(os.path.abspath(__file__))
    # Find all test files recursively in the workspace
    test_files = glob.glob(os.path.join(workspace_root, "**", "*_test.py"), recursive=True)
    
    if not test_files:
        print("No test files ending in '_test.py' were found in the workspace.")
        sys.exit(0)
    
    print(f"Found {len(test_files)} test suite(s):")
    for tf in test_files:
        relative_path = os.path.relpath(tf, workspace_root)
        print(f" - {relative_path}")
    print("-" * 50)
    
    failed_suites = []
    
    for tf in test_files:
        relative_path = os.path.relpath(tf, workspace_root)
        print(f"Running suite: {relative_path}...")
        
        # Run the test script as a separate subprocess
        result = subprocess.run([sys.executable, tf], capture_output=False)
        
        if result.returncode != 0:
            failed_suites.append(relative_path)
            print(f"[FAIL] {relative_path} failed!\n")
        else:
            print(f"[PASS] {relative_path} passed!\n")
            
    print("-" * 50)
    if failed_suites:
        print(f"Test Execution Failed! The following suites did not pass:")
        for fs in failed_suites:
            print(f" [FAIL] {fs}")
        sys.exit(1)
    else:
        print("All test suites passed successfully!")
        sys.exit(0)

if __name__ == '__main__':
    run_all_tests()
