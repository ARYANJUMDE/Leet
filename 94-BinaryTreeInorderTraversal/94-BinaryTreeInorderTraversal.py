# Last updated: 12/29/2025, 10:58:51 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        x=[]
        if root!=None:
            x=x+self.inorderTraversal(root.left)
            x.append(root.val)
            x=x+self.inorderTraversal(root.right)
        return x
    
        