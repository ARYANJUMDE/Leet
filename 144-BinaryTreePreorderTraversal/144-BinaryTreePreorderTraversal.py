# Last updated: 12/31/2025, 11:00:51 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def preorderTraversal(self, root):
9        x=[]
10        if root!=None:
11            x.append(root.val)
12            x=x+self.preorderTraversal(root.left)
13
14            x=x+self.preorderTraversal(root.right)
15
16        return x
17
18        