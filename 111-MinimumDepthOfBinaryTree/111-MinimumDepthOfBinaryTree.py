# Last updated: 1/26/2026, 11:28:32 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root==None:
            return 0
        lh=self.minDepth(root.left)
        rh=self.minDepth(root.right)
        
        if root.left==None:
            return rh+1

        if root.right==None:
            return lh+1
        
        return min(lh,rh)+1
        