# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1=d=ListNode(0)
        d.next = head
        while d.next and d.next.next:
            p =  d.next 
            q = d.next.next
            d.next,p.next,q.next = q,q.next,p
            d=p
        return d1.next
        