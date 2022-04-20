# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:#pointer
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
        

class Solution: #hashtable
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next


        while headA is not None:

            if headA in nodes_in_B:
                return headA
        
            headA = headA.next

        return None
        
        