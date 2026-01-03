# Last updated: 1/3/2026, 1:25:56 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseList(self, head):
8        curr=head
9        prev=None
10        while(curr!=None):
11            save=curr.next
12            curr.next=prev
13            prev=curr
14            curr=save
15        return prev
16        