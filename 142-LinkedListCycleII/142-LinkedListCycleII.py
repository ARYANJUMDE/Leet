# Last updated: 1/12/2026, 1:02:32 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def detectCycle(self, head):
9        slow=head
10        fast=head
11        while fast!=None and fast.next!=None:
12            slow=slow.next
13
14            fast=fast.next.next
15            if slow==fast:
16
17                break
18
19        else:
20            return None
21        ptr=head
22        while ptr!=slow:
23            ptr=ptr.next
24            slow=slow.next
25        return ptr
26
27        