# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        
        #a->b->c
        #c->b->a->null
        
        
        prev = None
        curr = head 
        
        while curr:
            next_temp = curr.next
            
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev