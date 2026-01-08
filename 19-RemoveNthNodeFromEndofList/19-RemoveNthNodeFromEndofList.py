# Last updated: 1/8/2026, 10:46:07 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def removeNthFromEnd(self, head, n):
8        count=0
9        curr=head
10        while curr!=None:
11            count=count+1
12            curr=curr.next
13        if head==None:
14            return None
15        if n==count:
16            return head.next  
17        
18        else:
19            
20            pos=count-n+1
21            i=1
22            curr2=head
23            while(i!=pos-1 and curr2.next!=None):
24                curr2=curr2.next
25                i=i+1
26            curr2.next=curr2.next.next
27            return head
28
29
30        