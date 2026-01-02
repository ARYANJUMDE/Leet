# Last updated: 1/2/2026, 3:23:15 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6# class Solution(object):
7#     def sortList(self,head):
8#         current=head
9#         while(current!=None):
10#             next_node=current.next
11#             while(next_node!=None):
12#                 if(current.val>next_node.val):
13#                     current.val,next_node.val=next_node.val,current.val
14#                 next_node=next_node.next
15#             current=current.next
16#         return head
17        
18class Solution(object):
19    def sortList(self, head):
20        # Base case: if the list is empty or has only one node
21        if not head or not head.next:
22            return head
23
24        # Step 1: Split list into two halves
25        slow, fast = head, head.next
26        while fast and fast.next:
27            slow = slow.next
28            fast = fast.next.next
29
30        mid = slow.next
31        slow.next = None  # Break the list into two halves
32
33        # Step 2: Sort both halves recursively
34        left = self.sortList(head)
35        right = self.sortList(mid)
36
37        # Step 3: Merge sorted halves
38        return self.merge(left, right)
39
40    def merge(self, l1, l2):
41        dummy = tail = ListNode(0)
42        while l1 and l2:
43            if l1.val < l2.val:
44                tail.next, l1 = l1, l1.next
45            else:
46                tail.next, l2 = l2, l2.next
47            tail = tail.next
48        tail.next = l1 or l2
49        return dummy.next
50
51        