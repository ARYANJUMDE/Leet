# Last updated: 1/26/2026, 11:28:33 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return (max(lh,rh)+1)
        