def subarraySum(self, nums, k):
    '''Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.'''
    

    count = 0

    for start in range(len(nums)):
        current_sum = 0
        for end in range(start,len(nums)):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
    return count

nums = [1,1,1]
k = 2
print(subarraySum(0, nums, k))