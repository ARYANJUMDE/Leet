# Last updated: 3/16/2026, 8:29:57 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x, next=None, random=None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution(object):
11    def copyRandomList(self, head):
12        
13        if not head:
14            return None
15        
16        oldToNew = {}
17        
18        curr = head
19        
20        # create copy of each node
21        while curr:
22            copy = Node(curr.val)
23            oldToNew[curr] = copy
24            curr = curr.next
25        
26        curr = head
27        
28        # assign next and random pointers
29        while curr:
30            copy = oldToNew[curr]
31            
32            copy.next = oldToNew.get(curr.next)
33            copy.random = oldToNew.get(curr.random)
34            
35            curr = curr.next
36        
37        return oldToNew[head]
38        