# Last updated: 1/14/2026, 1:21:46 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def minDepth(self, root):
9        if root==None:
10            return 0
11        lh=self.minDepth(root.left)
12        rh=self.minDepth(root.right)
13        
14        if root.left==None:
15            return rh+1
16
17        if root.right==None:
18            return lh+1
19        
20        return min(lh,rh)+1
21        