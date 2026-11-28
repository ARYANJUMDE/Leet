# Last updated: 11/28/2026, 11:55:57 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
9        result=[]
10        def inorder(root,x,sum1):
11            if root is None:
12                return 
13            x.append(root.val)
14            sum1=sum1+root.val
15            inorder(root.left,x,sum1)
16            inorder(root.right,x,sum1)
17            if root.left==None and root.right==None:
18                if sum1==targetSum:
19                    result.append(x[:])
20            sum1=sum1-x[-1]
21            x.pop()
22        inorder(root,[],0)
23        return result
24            
25
26        # from collections import deque
27        # queue=deque([])
28        # queue.append(root)
29        # result=[]
30        # while len(queue)>0:
31        #     t=len(queue)
32        #     x=[]
33        #     sum1=0
34        #     while t>0:
35        #         o=queue.popleft()
36        #         sum1=sum1+o.val
37        #         if o.left!=None:
38        #             queue.append(o.left)
39        #         if o.right!=None:
40        #             queue.append(o.right)
41        #         t=t-1
42        #     if sum1==targetSum:
43        #         result.append(x)
44        # return result
45
46
47        