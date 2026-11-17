# Last updated: 11/17/2026, 11:26:29 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def rightSideView(self, root):
9        if root==None:
10            return []
11        from collections import deque
12        queue=deque([])
13        result=[]
14        queue.append(root)
15        while len(queue)>0:
16            x=[]
17            t=len(queue)
18            while t>0:
19                p=queue.popleft()
20                x.append(p.val)
21                if p.left!=None:
22                    queue.append(p.left)
23                if p.right!=None:
24                    queue.append(p.right)
25                t=t-1
26            result.append(x[-1])
27        return result