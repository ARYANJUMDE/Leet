# Last updated: 1/26/2026, 11:28:27 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next

            fast=fast.next.next
            if slow==fast:

                break

        else:
            return None
        ptr=head
        while ptr!=slow:
            ptr=ptr.next
            slow=slow.next
        return ptr

        