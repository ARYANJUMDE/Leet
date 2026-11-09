# Last updated: 11/9/2026, 10:46:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
9        if root is None:
10            return []
11        queue=deque([])
12        queue.append(root)
13        ans=[]
14        while len(queue)>0:
15            result=[]
16            n=len(queue)
17            for i in range(n):
18                root=queue.popleft()
19                result.append(root.val)
20                if root.left!=None:
21                    queue.append(root.left)
22                if root.right!=None:
23                    queue.append(root.right)
24            ans.append(result)
25        return ans[::-1]
26        