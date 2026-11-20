# Last updated: 11/20/2026, 10:52:15 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def largestValues(self, root):
9        from collections import deque
10        if root==None:
11            return []
12        queue=deque([])
13        queue.append(root)
14        result=[]
15        while len(queue)>0:
16            x=[]
17            n=len(queue)
18            while n>0:
19                t=queue.popleft()
20                if len(x)==0:
21                    x.append(t.val)
22                else:
23                    if x[0]<t.val:
24                        x[0]=t.val
25                if t.left!=None:
26                    queue.append(t.left)
27                if t.right!=None:
28                    queue.append(t.right)
29                n=n-1
30            result.append(x[0])
31        return result
32        