# Last updated: 9/30/2026, 10:27:49 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution(object):
9    def maxLevelSum(self, root):
10        result=[]
11        queue=deque([])
12        queue.append(root)
13        while len(queue)>0:
14            level=[]
15            x=len(queue)
16            for i in range(x):
17                r=queue.popleft()
18                level.append(r.val)
19                if r.left!=None:
20                    queue.append(r.left)
21                if r.right!=None:
22                    queue.append(r.right)
23            result.append(sum(level))
24        t=max(result)
25        return result.index(t)+1
26        
27        
28
29
30        