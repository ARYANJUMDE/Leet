# Last updated: 11/13/2026, 4:55:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
9        result=[]
10        from collections import deque
11        queue=deque([])
12        queue.append(root)
13        while len(queue)>0:
14            x=queue.popleft()
15            if x.left!=None:
16                queue.append(x.left)
17                if x.left.left==None and x.left.right==None:
18                    result.append(x.left.val)
19            if x.right!=None:
20                queue.append(x.right)
21        return sum(result)
22        