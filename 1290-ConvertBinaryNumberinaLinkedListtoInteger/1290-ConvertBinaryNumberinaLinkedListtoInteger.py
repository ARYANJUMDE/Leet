# Last updated: 1/11/2026, 11:22:00 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def getDecimalValue(self, head):
8        x=[]
9        curr=head
10        while curr!=None:
11            x.append(curr.val)
12            curr=curr.next
13        
14        s=''
15        for num in x:
16            s=s+str(num)
17        
18        t=int(s,2)
19        return(t)
20             
21        