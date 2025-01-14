def twoSum(nums, target):
    #dictionary to store elements and their indices 
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        #check if the complement exists in the dictionary 
        if complement in num_indices:
            #if it does, return the indices 
            #of the current element and its complement 
            return [num_indices[complement], i]
        #if the complement doesn't exists 
        #add the current element and its index to the dictionary 
        num_indices[num] = i
    #if no solution found, return an empty list 
    return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))