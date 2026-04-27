# Last updated: 4/27/2026, 11:25:00 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution(object):
9    def lowestCommonAncestor(self, root, p, q):
10        if root is None:
11            return None
12        if root.val==p.val or root.val==q.val:
13            return root
14        left=self.lowestCommonAncestor(root.left,p,q)
15        right=self.lowestCommonAncestor(root.right,p,q)
16        if left is not None and right is not None:
17            
18            return root
19        if left is not None:
20            return left
21        else:
22            return right
23    
24        