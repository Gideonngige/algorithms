def search(nums, target):
    #initialize pointers
    left = 0
    right = len(nums) - 1

    #binary search
    while left <= right:
        #find middle element
        mid = (left + right ) // 2

        #if targte is founs
        if nums[mid] == target:
            return mid
        #if target is smaller search left half
        elif nums[mid] > target:
            right = mid - 1
        
        #if target is larger search right half
        else:
            left = mid + 1
    #target not found
    return -1

nums = [-1,0,3,5,9,12]
print(search(nums, 2))#print -1