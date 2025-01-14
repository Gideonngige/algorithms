def hasCycle(self, head):
    #handle empty list or single node 
    if not head or not head.next:
        return False
    
    #initialize slow and fast pointers
    slow = head 
    fast = head.next 

    #move pointers untill they meet or fast reaches end of list
    while slow != fast:
        #if fast pointer reaches end, no cycle exixts 
        if not fast or not fast.next:
            return False
        #move slow one step and fast two steps 
        slow = slow.next
        fast = fast.next.next
    #if we exit the loop, poimyers have met
    return True