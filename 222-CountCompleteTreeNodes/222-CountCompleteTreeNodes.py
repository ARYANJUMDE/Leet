# Last updated: 1/15/2026, 12:15:22 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def countNodes(self, root):
9        x=self.inorder(root)
10        return len(x)
11    def inorder(self,root):
12        x=[]
13        if root!=None:
14            x=x+self.inorder(root.left)
15            x.append(root.val)
16            x=x+self.inorder(root.right)
17        return x
18        