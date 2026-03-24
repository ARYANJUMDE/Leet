# Last updated: 3/24/2026, 3:07:09 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def isPalindrome(self, head):
8        # fast=head
9        # slow=head
10        # while fast!=None and fast.next!=None:
11        #     slow=slow.next
12        #     fast=fast.next.next
13        # mid=slow
14        # curr=mid
15        # prev=None
16        # while curr!=None:
17
18        #     save=curr.next
19        #     curr.next=prev
20        #     prev=curr
21        #     curr=save
22        # first=head
23        # second=prev
24        # while(second!=None):
25        #     if(first.val!=second.val):
26        #         return False
27        #     second=second.next
28        #     first=first.next
29        # return True
30
31        z=[]
32        p=[]
33        x=head
34        x2=None
35        q=head
36        while x!=None:
37            z.append(x.val)
38            x=x.next
39        while q!=None:
40            t=q.next
41            q.next=x2
42            x2=q
43            q=t
44        y=x2
45        while y!=None:
46            p.append(y.val)
47            y=y.next
48        if(z==p):
49            return(True)
50        else:
51            return(False)
52
53
54        
55
56
57        
58        