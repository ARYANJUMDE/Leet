# Last updated: 11/24/2026, 12:50:20 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        x=[-9999999]
10        max_count=0
11        def preorder(root):
12            nonlocal max_count
13            if root is None:
14                return
15            if max(x)<=root.val:
16                max_count=max_count+1
17            x.append(root.val)
18            preorder(root.left)
19            preorder(root.right)
20            x.pop()
21        preorder(root)
22        return max_count
23        # from collections import deque
24        # count=1
25        # queue=deque([])
26        # queue.append(root)
27        # result=[]
28        # while len(queue)>0:
29        #     x=[]
30        #     t=len(queue)
31        #     while t>0:
32        #         o=queue.popleft()
33        #         if o==0:
34        #             x.append(0)
35        #         else:
36        #             x.append(o.val)
37        #             if o.left!=None:
38        #                 queue.append(o.left)
39        #             elif o.left==None:
40        #                 queue.append(0)
41        #             if o.right!=None:
42        #                 queue.append(o.right)
43        #             elif o.right==None:
44        #                 queue.append(0)
45        #         if x==[0,0]:
46        #             break
47        #         elif len(x)==2 and x!=[0,0]:
48        #             result.append(x)
49        #             x=[]
50        #         t=t-1
51        # return result
52        # # for i in range(1,len(result)):
53        #     for j in range(0,i):
54
55        # for i in range(1,len(result)):
56        #     if result[0]<=result[i]:
57        #         count=count+1
58        # return count
59            
60            
61        