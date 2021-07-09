# It's not entirely clear how to best reference external files in tests

### recreate by following these steps

1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip3 install -r requirements.txt
4. pytest

### expectations:

Test 1 should pass it doesn't use an external file


Test 2 should fail because it depends on an external file
