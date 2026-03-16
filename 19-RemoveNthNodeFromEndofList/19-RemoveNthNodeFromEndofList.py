# Last updated: 3/16/2026, 8:26:57 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def partition(self, head, x):
8        beforeHead = ListNode(0)
9        afterHead = ListNode(0)
10        
11        before = beforeHead
12        after = afterHead
13        
14        while head:
15            if head.val < x:
16                before.next = head
17                before = before.next
18            else:
19                after.next = head
20                after = after.next
21            
22            head = head.next
23        
24        after.next = None
25        before.next = afterHead.next
26        
27        return beforeHead.next
28        