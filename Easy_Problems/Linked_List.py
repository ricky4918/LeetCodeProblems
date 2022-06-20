class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        
        #prev - 1- 2 - 3 -4
        
        prev = None
        curr = head
        
        while curr:
            
            next = curr.next
            
            curr.next = prev
            prev = curr
            curr = next
            
            
        return prev
            
            