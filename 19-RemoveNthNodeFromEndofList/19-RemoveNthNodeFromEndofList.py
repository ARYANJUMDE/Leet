# Last updated: 3/16/2026, 8:25:04 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        dummy = ListNode(0)
9        dummy.next = head
10        prev = dummy
11        
12        while head:
13            
14            if head.next and head.val == head.next.val:
15                
16                while head.next and head.val == head.next.val:
17                    head = head.next
18                
19                prev.next = head.next
20            
21            else:
22                prev = prev.next
23            
24            head = head.next
25        
26        return dummy.next