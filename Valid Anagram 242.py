def valid_anagram(s1, s2):
    """
    Check if two strings are anagrams of each other.

    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        bool: True if s1 and s2 are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Sort the characters of both strings and compare
    return sorted(s1) == sorted(s2)