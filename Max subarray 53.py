def max_subarray(arr):

    current_max = arr[0]
    max_so_far = arr[0]                            
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

# Here the sum of the contiguous subarray [4,-1,2,1] has the largest sum = 6.