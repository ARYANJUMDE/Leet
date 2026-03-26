# Last updated: 3/26/2026, 8:44:56 PM
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
12        if root.val<p.val and root.val<q.val:
13            return self.lowestCommonAncestor(root.right,p,q)
14        if root.val>p.val and root.val>q.val:
15            return self.lowestCommonAncestor(root.left,p,q)
16        return root
17
18        