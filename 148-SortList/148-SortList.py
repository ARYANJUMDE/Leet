# Last updated: 12/27/2025, 6:57:59 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def sortList(self,head):
#         current=head
#         while(current!=None):
#             next_node=current.next
#             while(next_node!=None):
#                 if(current.val>next_node.val):
#                     current.val,next_node.val=next_node.val,current.val
#                 next_node=next_node.next
#             current=current.next
#         return head
        
class Solution(object):
    def sortList(self, head):
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head

        # Step 1: Split list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # Break the list into two halves

        # Step 2: Sort both halves recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

        