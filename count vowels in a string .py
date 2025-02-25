def count_vowels(string):
    s=list(string.lower())
    vowels=set("aeiou")
    l=[i for i in s if  i in vowels]
    return len(l)

def test_count_vowels():
    # Test case 1: Standard string with vowels
    result = count_vowels("Hello World!")
    assert result == 3, f"Expected 3, but got {result}"
    
    # Test case 2: Empty string (no vowels)
    result = count_vowels("")
    assert result == 0, f"Expected 0, but got {result}"
    
    # Test case 3: String with no vowels
    result = count_vowels("bcdfg")
    assert result == 0, f"Expected 0, but got {result}"
    
    # Test case 4: String with all vowels
    result = count_vowels("aeiou")
    assert result == 5, f"Expected 5, but got {result}"
    
    # Test case 5: Mixed case string with vowels
    result = count_vowels("aEiOu")
    assert result == 5, f"Expected 5, but got {result}"
    
    # Test case 6: String with special characters and spaces
    result = count_vowels("Hello, @world!")
    assert result == 3, f"Expected 3, but got {result}"
    
    # Test case 7: String with numbers and vowels
    result = count_vowels("1234aA")
    assert result == 2, f"Expected 2, but got {result}"

    print("All test cases passed!")

# Run the test
test_count_vowels()


