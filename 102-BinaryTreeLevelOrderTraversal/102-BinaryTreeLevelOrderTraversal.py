# Last updated: 3/26/2026, 8:38:52 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isValidBST(self, root):
9        
10        def check(node, low, high):
11            if node is None:
12                return True
13            
14            if not (low < node.val < high):
15                return False
16            
17            return (check(node.left, low, node.val) and
18                    check(node.right, node.val, high))
19        
20        return check(root, float('-inf'), float('inf'))        