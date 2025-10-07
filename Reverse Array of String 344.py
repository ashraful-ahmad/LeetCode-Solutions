def reverse_string(s):
    """Return the reverse of the input array of strings whithout creating a new array."""
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# Example usage:
input_array = ["h", "e", "l", "l", "o"]
print(reverse_string(input_array))