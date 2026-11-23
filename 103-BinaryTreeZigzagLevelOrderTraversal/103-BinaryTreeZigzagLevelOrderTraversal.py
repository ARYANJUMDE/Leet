# Last updated: 11/23/2026, 10:48:12 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
9        if root is None:
10            return []
11        from collections import deque
12        queue=deque([])
13        queue.append(root)
14        result=[]
15        while len(queue)>0:
16            t=len(queue)
17            x=[]
18            while t>0:
19                p=queue.popleft()
20                x.append(p.val)
21                if p.left!=None:
22                    queue.append(p.left)
23                if p.right!=None:
24                    queue.append(p.right)
25                t=t-1
26            result.append(x)
27        o=[]
28        for i in range(len(result)):
29            if i%2==0:
30                o.append(result[i])
31            else:
32                o.append(result[i][::-1])
33        return o