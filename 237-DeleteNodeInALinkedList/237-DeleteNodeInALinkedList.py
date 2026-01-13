# Last updated: 1/13/2026, 2:57:54 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
        # curr=head
        # while curr.val!=node:
        #     curr=curr.next
        # curr.next=curr.next.next

        # return head
        