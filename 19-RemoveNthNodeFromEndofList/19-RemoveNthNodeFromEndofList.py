# Last updated: 3/16/2026, 8:23:16 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def rotateRight(self, head, k):
8        if not head or not head.next:
9            return head
10        
11        # find length
12        length = 1
13        tail = head
14        
15        while tail.next:
16            tail = tail.next
17            length += 1
18        
19        k = k % length
20        if k == 0:
21            return head
22        
23        # make circular list
24        tail.next = head
25        
26        # find new tail
27        steps = length - k
28        newTail = head
29        
30        for i in range(steps-1):
31            newTail = newTail.next
32        
33        # new head
34        newHead = newTail.next
35        
36        # break circle
37        newTail.next = None
38        
39        return newHead