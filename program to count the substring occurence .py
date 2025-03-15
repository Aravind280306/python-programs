#program to count the substring occurence
def count_substring_occurrences(string,substring):
    result=0
    result=string.count(substring)
    return result


def test_count_substring_occurrences():
    # Test 1: Basic case
    result = count_substring_occurrences('hello world', 'world')
    print(f"Test 1 - Basic case: {'Passed' if result == 1 else 'Failed'}")
    
    # Test 2: Substring occurs multiple times
    result = count_substring_occurrences('hello world world', 'world')
    print(f"Test 2 - Multiple occurrences: {'Passed' if result == 2 else 'Failed'}")
    
    # Test 3: Substring not found
    result = count_substring_occurrences('hello world', 'Python')
    print(f"Test 3 - Substring not found: {'Passed' if result == 0 else 'Failed'}")
    
    # Test 4: Empty string
    result = count_substring_occurrences('', 'world')
    print(f"Test 4 - Empty string: {'Passed' if result == 0 else 'Failed'}")
    
    # Test 5: Substring is empty
    result = count_substring_occurrences('hello world','')
    print(f"Test 5 - Substring is empty: {'Passed' if result == 0 else 'Failed'}")
    
    # Test 6: Substring is the same as the whole string
    result = count_substring_occurrences('hello', 'hello')
    print(f"Test 6 - Substring is the same as the whole string: {'Passed' if result == 1 else 'Failed'}")
    
    # Test 7: Case sensitivity
    result = count_substring_occurrences('Hello world', 'hello')
    print(f"Test 7 - Case sensitivity: {'Passed' if result == 0 else 'Failed'}")
    
    # Test 8: Substring is longer than the string
    result = count_substring_occurrences('hello', 'hello world')
    print(f"Test 8 - Substring longer than the string: {'Passed' if result == 0 else 'Failed'}")
    
    # Test 9: Substring is a single character
    result = count_substring_occurrences('hello world', 'o')
    print(f"Test 9 - Single character substring: {'Passed' if result == 2 else 'Failed'}")
    
# Run the tests
test_count_substring_occurrences()


