def check_str(s: str):
    normalized_s = ''.join(char.lower() for char in s if char.isalnum())

    # Use two pointers to check for palindrome
    left, right = 0, len(normalized_s) - 1

    while left < right:
        if normalized_s[left] != normalized_s[right]:
            return False
        left += 1
        right -= 1

    return True