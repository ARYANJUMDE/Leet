# Last updated: 3/26/2026, 8:24:18 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8
9class Solution(object):
10    def levelOrder(self, root):
11        if root is None:
12            return []
13        
14        result = []
15        q = deque([root])
16        
17        while q:
18            level = []
19            size = len(q)
20            
21            for i in range(size):
22                node = q.popleft()
23                level.append(node.val)
24                
25                if node.left:
26                    q.append(node.left)
27                if node.right:
28                    q.append(node.right)
29            
30            result.append(level)
31        
32        return result
33        