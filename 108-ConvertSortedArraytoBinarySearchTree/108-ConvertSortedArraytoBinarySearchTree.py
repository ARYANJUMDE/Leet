# Last updated: 3/7/2026, 10:25:46 AM
1# class TreeNode(object):
2#     def __init__(self, val=0, left=None, right=None):
3#         self.val = val
4#         self.left = left
5#         self.right = right
6class Solution(object):
7    def sortedArrayToBST(self, nums):
8        if not nums:
9            return None
10        mid=len(nums)//2
11        root=TreeNode(nums[mid])
12        root.left=self.sortedArrayToBST(nums[:mid])
13        root.right=self.sortedArrayToBST(nums[mid+1:])
14        return root
15        