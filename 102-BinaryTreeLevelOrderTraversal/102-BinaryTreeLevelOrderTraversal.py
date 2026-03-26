# Last updated: 3/26/2026, 8:37:00 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def buildTree(self, preorder, inorder):
9        if not preorder or not inorder:
10            return None
11        
12        inorder_map = {val: i for i, val in enumerate(inorder)}
13        
14        self.pre_idx = 0
15        
16        def helper(left, right):
17            if left > right:
18                return None
19            
20            
21            root_val = preorder[self.pre_idx]
22            self.pre_idx += 1
23            
24            root = TreeNode(root_val)
25            
26            
27            index = inorder_map[root_val]
28            
29            
30            root.left = helper(left, index - 1)
31            root.right = helper(index + 1, right)
32            
33            return root
34        
35        return helper(0, len(inorder) - 1)
36        