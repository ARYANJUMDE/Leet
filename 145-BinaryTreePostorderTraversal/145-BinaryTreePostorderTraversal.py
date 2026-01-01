# Last updated: 1/1/2026, 10:44:55 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def postorderTraversal(self, root):
9        x=[]
10        if root!=None:
11            x=x+self.postorderTraversal(root.left)
12            x=x+self.postorderTraversal(root.right)
13            
14            x.append(root.val)
15        return x
16
17        