# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        
        while f:
                if not f.next or not f.next.next:
                    return False
                s = s.next
                f = f.next.next
                if s == f:
                    return True
        return False