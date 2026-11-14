# Last updated: 11/14/2026, 1:27:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: TreeNode | None) -> int:
9        if root is None:
10            return 0
11        x=[]
12        def sum_leaf(root,st):
13            if root is None:
14                return
15            if root.left is None and root.right is None:
16                x.append(int(st+str(root.val)))
17            sum_leaf(root.left,st+str(root.val))
18            sum_leaf(root.right,st+str(root.val))
19        sum_leaf(root,"")
20        return sum(x)
21
22
23            
24        # from collections import deque
25        # ans=[]
26        # queue=deque([])
27        # queue.append(root)
28        # while len(queue)>0:
29        #     result=[]
30        #     n=len(queue)
31        #     while n>0:
32        #         x=queue.popleft()
33        #         if x==-1:
34        #             result.append(-1)
35        #         else:
36        #             result.append(x.val)
37        #             if x.left!=None:
38        #                 queue.append(x.left)
39        #             else:
40        #                 queue.append(-1)
41        #             if x.right!=None:
42        #                 queue.append(x.right)
43        #             else:
44        #                 queue.append(-1)
45        #         n=n-1
46        #     ans.append(result)
47        # return ans
48
49
50        