# Last updated: 3/26/2026, 8:46:46 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def deleteNode(self, root, key):
9        if root is None:
10            return None
11        
12        if key < root.val:
13            root.left = self.deleteNode(root.left, key)
14        
15        elif key > root.val:
16            root.right = self.deleteNode(root.right, key)
17        
18        else:
19            if root.left is None:
20                return root.right
21            if root.right is None:
22                return root.left
23            
24            temp = root.right
25            while temp.left:
26                temp = temp.left
27            
28            root.val = temp.val
29            
30            root.right = self.deleteNode(root.right, temp.val)
31        
32        return root        