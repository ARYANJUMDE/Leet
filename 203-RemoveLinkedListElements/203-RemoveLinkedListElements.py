# Last updated: 1/9/2026, 4:48:55 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def removeElements(self, head, val):
8        x=[]
9        curr=head
10        while curr!=None:
11            if(curr.val!=val):
12                x.append(curr.val)
13            curr=curr.next
14        dummy=ListNode(0)
15        temp=dummy
16        for num in x:
17            temp.next=ListNode(num)
18            temp=temp.next
19        return dummy.next
20        
21
22
23        