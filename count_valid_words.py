def countValidWords(s):
    """
    Identify the number of valid words in a given string.
    A word is considered valid if it meets all of the following criteria:
    - Contains at least 3 characters
    - Contains only alphanumeric characters (letters 'a'-'z', 'A'-'Z', and numbers 0-9)
    - Includes at least one vowel ('a', 'e', 'i', 'o', 'u')
    - Includes at least one consonant (any letter that is not a vowel)
    
    Args:
        s: a string to analyze
    
    Returns:
        int: the number of valid words in s
    """
    if not s:
        return 0
    
    # Split the string into words (by spaces)
    words = s.split()
    valid_count = 0
    
    vowels = set('aeiouAEIOU')
    
    for word in words:
        # Check if word has at least 3 characters
        if len(word) < 3:
            continue
        
        # Check if word contains only alphanumeric characters
        if not word.isalnum():
            continue
        
        # Check if word has at least one vowel and one consonant
        has_vowel = False
        has_consonant = False
        
        for char in word:
            if char.isalpha():  # Only check letters for vowel/consonant
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        # Word is valid if it has both at least one vowel and one consonant
        if has_vowel and has_consonant:
            valid_count += 1
    
    return valid_count


# Test cases
if __name__ == "__main__":
    # Test case 1: "This is Form16 submission date"
    test1 = "This is Form16 submission date"
    result1 = countValidWords(test1)
    print(f"Input: '{test1}'")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print()
    
    # Test case 2: "Alex wins the game"
    test2 = "Alex wins the game"
    result2 = countValidWords(test2)
    print(f"Input: '{test2}'")
    print(f"Output: {result2}")
    print(f"Expected: 4")
    print()
    
    # Additional test case from the original example
    test3 = "This is an example string 234"
    result3 = countValidWords(test3)
    print(f"Input: '{test3}'")
    print(f"Output: {result3}")
    print(f"Expected: 3 (This, example, string)")
    
    # Test edge cases
    test4 = "a ab abc"
    result4 = countValidWords(test4)
    print(f"Input: '{test4}'")
    print(f"Output: {result4}")
    print(f"Expected: 0 (all too short or missing vowel/consonant)")
    print()
    
    test5 = "hello world test123"
    result5 = countValidWords(test5)
    print(f"Input: '{test5}'")
    print(f"Output: {result5}")
    print(f"Expected: 3 (hello, world, test123)")