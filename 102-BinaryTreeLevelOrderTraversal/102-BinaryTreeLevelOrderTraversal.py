# Last updated: 3/26/2026, 8:53:38 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxPathSum(self, root):
9        self.max_sum=float('-inf')
10        def dfs(node):
11            if not node:
12                return 0
13            left=max(dfs(node.left),0)
14            right=max(dfs(node.right),0)
15            self.max_sum=max(self.max_sum,left+right+node.val)
16            return node.val+max(left,right)
17
18        dfs(root)
19        return self.max_sum
20        