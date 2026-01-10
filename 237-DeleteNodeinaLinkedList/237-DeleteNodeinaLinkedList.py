# Last updated: 1/10/2026, 9:29:06 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def deleteNode(self, node):
9        node.val=node.next.val
10        node.next=node.next.next
11        # curr=head
12        # while curr.val!=node:
13        #     curr=curr.next
14        # curr.next=curr.next.next
15
16        # return head
17        