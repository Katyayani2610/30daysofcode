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


# Example usage and test cases
if __name__ == "__main__":
    # Test with the provided examples
    print(countValidWords("This is Form16 submis$ion date"))  # Output: 3
    print(countValidWords("Alex wins the game"))              # Output: 4
    print(countValidWords("This is an example string 234"))   # Output: 3