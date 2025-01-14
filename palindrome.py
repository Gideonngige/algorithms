def isPalindrome(s:str) -> bool:
    left, right = 0, len(s) - 1 

    while left < right:
        #skip left if not alphanumeric 
        if not s[left].isalnum():
            left += 1
        #skip right if not alphanumeric 
        elif not s[right].isalnum():
            right -= 1 
        #convert to lowercase and compare
        elif s[left].lower() != s[right].lower():
            return False
        #move both pointers 
        else:
            left += 1
            right -= 1
    return True

s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome(s2))