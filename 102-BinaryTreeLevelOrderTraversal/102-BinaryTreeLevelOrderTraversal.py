# Last updated: 3/26/2026, 8:34:57 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def diameterOfBinaryTree(self, root):
9        self.diameter = 0
10        
11        def height(node):
12            if node is None:
13                return 0
14            
15            left = height(node.left)
16            right = height(node.right)
17            
18            self.diameter = max(self.diameter, left + right)
19            
20            return 1 + max(left, right)
21        
22        height(root)
23        return self.diameter        