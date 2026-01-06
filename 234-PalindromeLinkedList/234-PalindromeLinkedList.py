# Last updated: 1/6/2026, 3:45:12 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def isPalindrome(self, head):
8        fast=head
9        slow=head
10        while fast!=None and fast.next!=None:
11            slow=slow.next
12            fast=fast.next.next
13        mid=slow
14        curr=mid
15        prev=None
16        while curr!=None:
17
18            save=curr.next
19            curr.next=prev
20            prev=curr
21            curr=save
22        first=head
23        second=prev
24        while(second!=None):
25            if(first.val!=second.val):
26                return False
27            second=second.next
28            first=first.next
29        return True
30
31
32        
33        