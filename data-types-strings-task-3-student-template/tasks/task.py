def replacer(s: str) -> str:
    """
    Add your code here
    """
    temp_placeholder = "TEMP_PLACEHOLDER"
    s = s.replace('"', temp_placeholder)

    # Replace all ' with "
    s = s.replace("'", '"')

    # Replace the temporary placeholder with '
    s = s.replace(temp_placeholder, "'")

    return s
