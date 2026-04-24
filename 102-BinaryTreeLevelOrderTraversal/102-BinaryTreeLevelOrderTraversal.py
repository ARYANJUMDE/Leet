# Last updated: 4/24/2026, 12:09:52 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def levelOrder(self, root):
9        if root is None:
10            return []
11        queue=deque()
12        result=[]
13        
14        queue.append(root)
15        while queue:
16            level_size=len(queue)
17            level=[]
18            for i in range(level_size):
19                node=queue.popleft()
20                level.append(node.val)
21                if node.left:
22                    queue.append(node.left)
23                if node.right:
24                    queue.append(node.right)
25            result.append(level)
26        return result
27    
28        