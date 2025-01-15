def majorityElement(nums):
    #intialize count and candidate 
    count = 0
    candidate = None 

    #Boyer-Moore Voting Algorithm
    for num in nums:
        #if count is o, pick new candidate
        if count == 0:
            candidate = num
        
        #update count based whether the candidate is the same or different
        count += 1 if num == candidate else -1
    
    #return the majority element
    return candidate

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))