# Last updated: 1/5/2026, 5:35:21 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        x=[]
9        curr=head
10        while curr!=None:
11            if curr.val not in x:
12                x.append(curr.val)
13                
14            curr=curr.next
15        dummy=ListNode(0)
16        temp=dummy
17
18        for num in x:
19            temp.next=ListNode(num)
20            temp=temp.next
21        return dummy.next
22
23
24
25        