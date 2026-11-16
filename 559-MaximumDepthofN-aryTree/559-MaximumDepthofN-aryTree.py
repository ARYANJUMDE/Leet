# Last updated: 11/16/2026, 11:09:54 AM
1"""
2# Definition for a Node.
3class Node(object):
4    def __init__(self, val=None, children=None):
5        self.val = val
6        self.children = children
7"""
8
9class Solution(object):
10    def maxDepth(self, root):
11        if root is None:
12            return 0
13        from collections import deque
14        queue=deque([])
15        result=[]
16        queue.append(root)
17        while len(queue)>0:
18            x=[]
19            t=len(queue)
20            while t>0:
21                o=queue.popleft()
22                x.append(o.val)
23                for i in o.children:
24                    queue.append(i)
25                t=t-1
26            result.append(x)
27        return len(result)
28        