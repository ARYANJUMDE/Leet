# Last updated: 3/16/2026, 8:21:49 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def swapPairs(self, head):
8        dummy = ListNode(0)
9        dummy.next = head
10        
11        prev = dummy
12        
13        while prev.next and prev.next.next:
14            
15            first = prev.next
16            second = prev.next.next
17            
18            # swap
19            first.next = second.next
20            second.next = first
21            prev.next = second
22            
23            prev = first
24            
25        return dummy.next
26        