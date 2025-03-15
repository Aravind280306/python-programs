#program to replace substring in a given strings

def replace_substring(string,substring,newstring):
    result=string.replace(substring,newstring)
    return result

def test_replace_substring():
    # Test 1: Basic replacement
    result = replace_substring('hello world', 'world', 'Python')
    print(f"Test 1 - Basic replacement: {'Passed' if result == 'hello Python' else 'Failed'}")
    
    # Test 2: No occurrence of the old substring
    result = replace_substring('hello world', 'Java', 'Python')
    print(f"Test 2 - No occurrence of old substring: {'Passed' if result == 'hello world' else 'Failed'}")
    
    # Test 3: Multiple occurrences
    result = replace_substring('hello world world', 'world', 'Python')
    print(f"Test 3 - Multiple occurrences: {'Passed' if result == 'hello Python Python' else 'Failed'}")
    
    # Test 4: Empty string
    result = replace_substring('', 'world', 'Python')
    print(f"Test 4 - Empty string: {'Passed' if result == '' else 'Failed'}")
    
    # Test 5: Replacing with empty string
    result = replace_substring('hello world', 'world', '')
    print(f"Test 5 - Replacing with empty string: {'Passed' if result == 'hello ' else 'Failed'}")
    
    # Test 6: Old substring is empty
    result = replace_substring('hello world', '', 'Python')
    print(f"Test 6 - Old substring is empty: {'Passed' if result == 'hello world' else 'Failed'}")
    
    # Test 7: New substring is empty
    result = replace_substring('hello world', 'world', '')
    print(f"Test 7 - New substring is empty: {'Passed' if result == 'hello ' else 'Failed'}")
    
    # Test 8: Case sensitivity
    result = replace_substring('Hello World', 'world', 'Python')
    print(f"Test 8 - Case sensitivity: {'Passed' if result == 'Hello World' else 'Failed'}")

# Run the tests
test_replace_substring()


