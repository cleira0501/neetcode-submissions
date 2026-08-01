# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def print_list(self, node, list_name="List"):
    #     values = []
    #     curr = node
    #     while curr:
    #         values.append(str(curr.val))
    #         curr = curr.next
    #     print(f"{list_name}: {' -> '.join(values)}")

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
      
        head1 = list1
        head2 = list2

        if head1.val <= head2.val:
            
            head1.next = self.mergeTwoLists(head1.next,head2)
            return head1
        else:
            
            head2.next = self.mergeTwoLists(head2.next, head1)
            return head2
        


        