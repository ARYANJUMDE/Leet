# Last updated: 3/26/2026, 8:32:08 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        
10        def check(node):
11            if node is None:
12                return 0  
13            
14            left = check(node.left)
15            if left == -1:
16                return -1
17            
18            right = check(node.right)
19            if right == -1:
20                return -1
21            
22            if abs(left - right) > 1:
23                return -1
24            
25            return 1 + max(left, right)
26        
27        return check(root) != -1        