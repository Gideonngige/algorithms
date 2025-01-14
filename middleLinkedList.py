def middleNode(head):
    #initialize slow and fast pointers 
    slow = fast = head 
    #move pointers untill fast reaches the end 
    while fast and fast.next:
        #move slow pointer one step 
        slow = slow.next 
        #move fast pointer two steps 
        fast = fast.next.next
    return slow 
    
head = [1, 2, 3, 4, 5]
print(middleNode(head))