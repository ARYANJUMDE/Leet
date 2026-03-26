# Last updated: 3/26/2026, 8:26:08 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8
9class Solution(object):
10    def rightSideView(self, root):
11        if root is None:
12            return []
13        
14        result = []
15        q = deque([root])
16        
17        while q:
18            size = len(q)
19            
20            for i in range(size):
21                node = q.popleft()
22                
23                if i == size - 1:
24                    result.append(node.val)
25                
26                if node.left:
27                    q.append(node.left)
28                if node.right:
29                    q.append(node.right)
30        
31        return result
32        