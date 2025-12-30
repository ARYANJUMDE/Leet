# Last updated: 12/30/2025, 10:38:32 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxDepth(self, root):
9        if root is None:
10            return 0
11
12        lh=self.maxDepth(root.left)
13        rh=self.maxDepth(root.right)
14        return (max(lh,rh)+1)
15        