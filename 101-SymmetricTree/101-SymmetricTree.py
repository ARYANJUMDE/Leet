# Last updated: 11/11/2026, 1:14:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        from collections import deque
10        queue=deque([])
11        queue.append(root)
12        while len(queue)>0:
13            result=[]
14            y=len(queue)
15            for i in range(y):
16                x=queue.popleft()
17                if x==None:
18                    result.append(-99999)
19                else:
20                    result.append(x.val)
21                    if x.left!=None:
22                        queue.append(x.left)
23                    elif(x.left==None):
24                        queue.append(None)
25                    if x.right!=None:
26                        queue.append(x.right)
27                    elif(x.right==None):
28                        queue.append(None)
29            if result[:len(result)//2]!=result[(len(result)+1)//2:][::-1]:
30                return False
31        return True
32
33
34                
35
36
37