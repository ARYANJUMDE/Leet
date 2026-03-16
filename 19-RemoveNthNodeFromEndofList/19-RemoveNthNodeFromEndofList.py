# Last updated: 3/16/2026, 8:31:21 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reorderList(self, head):
8        if not head or not head.next:
9            return
10        
11        # 1. Find middle
12        slow = head
13        fast = head
14        
15        while fast and fast.next:
16            slow = slow.next
17            fast = fast.next.next
18        
19        # 2. Reverse second half
20        prev = None
21        curr = slow.next
22        slow.next = None
23        
24        while curr:
25            temp = curr.next
26            curr.next = prev
27            prev = curr
28            curr = temp
29        
30        # 3. Merge two lists
31        first = head
32        second = prev
33        
34        while second:
35            temp1 = first.next
36            temp2 = second.next
37            
38            first.next = second
39            second.next = temp1
40            
41            first = temp1
42            second = temp2
43        