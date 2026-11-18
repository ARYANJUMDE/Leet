# Last updated: 11/18/2026, 11:05:45 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def findBottomLeftValue(self, root):
9        from collections import deque
10        queue=deque([])
11        queue.append(root)
12        result=[]
13        while len(queue)>0:
14            x=[]
15            t=len(queue)
16            while t>0:
17                p=queue.popleft()
18                x.append(p.val)
19                if p.left!=None:
20                    queue.append(p.left)
21                if p.right!=None:
22                    queue.append(p.right)
23                t=t-1
24            result.append(x)
25        return result[-1][0]