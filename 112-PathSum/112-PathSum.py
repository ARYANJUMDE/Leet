# Last updated: 4/26/2026, 10:46:17 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def hasPathSum(self, root, targetSum):
9        if root is None:
10            return False
11        if root.left is None and root.right is None:
12            return root.val==targetSum
13        return(self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val))
14    
15        