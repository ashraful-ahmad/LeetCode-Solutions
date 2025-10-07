def two_sum_2(numbers, target):
    "Here the input array is sorted and Indexing starts at 1"

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return (left + 1, right + 1)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum_2(nums, target))
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/