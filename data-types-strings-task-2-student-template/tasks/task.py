def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    words = s.split()

    # Initialize the longest word as an empty string
    longest_word = ""

    # Iterate through the words to find the longest one
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
