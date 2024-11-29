def longestPalindrome(s: str) -> int:
    from collections import Counter
    
    # Step 1: Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Step 2: Initialize the length of the palindrome
    palindrome_length = 0
    odd_found = False
    
    # Step 3: Traverse the frequency dictionary
    for count in char_count.values():
        if count % 2 == 0:
            palindrome_length += count
        else:
            palindrome_length += count - 1
            odd_found = True
    
    # Step 4: If any character had an odd count, we can place one in the center
    if odd_found:
        palindrome_length += 1
    
    return palindrome_length

# Example usage
print(longestPalindrome("abccccdd"))  # Output: 7
print(longestPalindrome("a"))         # Output: 1





