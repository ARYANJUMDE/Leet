# Last updated: 11/12/2026, 1:09:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
9        from collections import deque
10        result=set()
11        queue=deque([])
12        queue.append(root)
13        while(len(queue))>0:
14            x=queue.popleft()
15            result.add(x.val)
16            if x.left!=None:
17                queue.append(x.left)
18            if x.right!=None:
19                queue.append(x.right)
20        t=list(result)
21        t.sort()
22        return t[k-1]
23
24