# Last updated: 1/4/2026, 11:45:58 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def hasCycle(self, head):
9        fast=head
10        slow=head
11        while fast!=None and fast.next!=None:
12            slow=slow.next
13            fast=fast.next.next
14            if(slow==fast):
15                return True
16        return False
17        