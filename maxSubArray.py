def maxSubArray(nums) -> int:
    #maximum sum so far 
    max_sum = nums[0]
    #maximum sum for subarray ending at current index 
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        #if maximum sum subarray ending at last
        #indx is negative, start a new subarray 
        if curr_sum < 0:
            curr_sum = nums[i]
        #otherwise extend the maximum sum
        #subarray from the last index 
        else:
            curr_sum = curr_sum + nums[i]
        #update the maximum sum if the current sum is greater 
        max_sum = max(max_sum, curr_sum)
    #max_sum now holds the maximum of all subarrays
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5, 4, -1, 7, 8]
print(maxSubArray(nums2))
        
