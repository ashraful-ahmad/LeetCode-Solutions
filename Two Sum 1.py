def twosum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None

ls = [2, 7, 11, 15]
print(twosum(ls, 9))  # Output: (0, 1)