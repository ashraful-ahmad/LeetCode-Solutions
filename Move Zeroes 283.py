def move_zeroes(arr):
    """
    Move all zeroes in the array to the end while maintaining the order of non-zero elements.

    Args:
        arr (list): List of integers.

    Returns:
        list: Modified list with zeroes moved to the end.
    """
    for i in arr[:]:
        if i == 0:
            arr.remove(0)
            arr.append(0)
        else:
            i + 1
    return arr

# Example usage:
input_array = [0, 0, 1, 0, 3, 12]
print(move_zeroes(input_array))