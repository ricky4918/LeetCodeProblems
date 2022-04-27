# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Queue import PriorityQueue

class Solution:
    #Brute Force
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        


        arr = []

        for nlist in lists:

            while nlist:

                arr.append(nlist.val)
                nlist = nlist.next

        head = curr = None
        for val in sorted(arr):

            if not curr:

                head = curr = ListNode(val)
            else:
                curr.next = ListNode(val)
                curr = curr.next

        return head
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        head = curr = ListNode(-1)

        q = PriorityQueue()
        for i,l in enumerate(lists):
            if l :
                q.put((l.val, i, l))

            while not q.empty():
                val, i, node = q.get()
                curr.next = ListNode(val)
                curr = curr.next
                node = node.next
                if node:
                    q.pu((node.val, i, node))

        return head.next

                