def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
                

def test_anagrams():
    # Test 1: Anagrams
    result = are_anagrams('listen', 'silent')
    print(f"Test 1 - Anagrams: {'Passed' if result else 'Failed'}")
    
    # Test 2: Anagrams
    result = are_anagrams('evil', 'vile')
    print(f"Test 2 - Anagrams: {'Passed' if result else 'Failed'}")
    
    # Test 3: Anagrams
    result = are_anagrams('earth', 'heart')
    print(f"Test 3 - Anagrams: {'Passed' if result else 'Failed'}")
    
    # Test 4: Not anagrams
    result = are_anagrams('hello', 'world')
    print(f"Test 4 - Not Anagrams: {'Passed' if not result else 'Failed'}")
    
    # Test 5: Not anagrams
    result = are_anagrams('python', 'java')
    print(f"Test 5 - Not Anagrams: {'Passed' if not result else 'Failed'}")
    
    # Test 6: Different length strings
    result = are_anagrams('abc', 'abcd')
    print(f"Test 6 - Not Anagrams (Different length): {'Passed' if not result else 'Failed'}")
    
    # Test 7: Empty strings
    result = are_anagrams('', '')
    print(f"Test 7 - Empty strings: {'Passed' if result else 'Failed'}")
    
    # Test 8: Case sensitivity
    result = are_anagrams('Hello', 'hello')
    print(f"Test 8 - Case sensitivity: {'Passed' if  result else 'Failed'}")
    
    # Test 9: Special characters
    result = are_anagrams('a!b@c#', '#b@c!a')
    print(f"Test 9 - Special characters: {'Passed' if result else 'Failed'}")
    
# Run the tests
test_anagrams()


