# Last updated: 3/16/2026, 8:28:44 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseBetween(self, head, left, right):
8        
9        dummy = ListNode(0)
10        dummy.next = head
11        prev = dummy
12        
13        # move prev to node before 'left'
14        for i in range(left-1):
15            prev = prev.next
16        
17        curr = prev.next
18        
19        # reverse the part
20        for i in range(right-left):
21            temp = curr.next
22            curr.next = temp.next
23            temp.next = prev.next
24            prev.next = temp
25        
26        return dummy.next