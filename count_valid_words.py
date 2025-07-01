def countValidWords(s: str) -> int:
    vowels = set("aeiouAEIOU")
    valid_count = 0

    for word in s.split():
        # Check for alphanumeric only
        if not word.isalnum():
            continue

        # Must be at least 3 characters
        if len(word) < 3:
            continue

        # Check for vowels and consonants
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch in vowels:
                has_vowel = True
            elif ch.isalpha():
                has_consonant = True

        if has_vowel and has_consonant:
            valid_count += 1

    return valid_count


# Test the function
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "hello world test",
        "abc def ghi",
        "a bc defg",
        "123 abc def",
        "hello! world?",
        "programming is fun",
        "a e i o u"
    ]
    
    for test_str in test_strings:
        result = countValidWords(test_str)
        print(f"Input: '{test_str}' -> Valid words: {result}")