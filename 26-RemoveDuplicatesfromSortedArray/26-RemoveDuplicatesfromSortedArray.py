# Last updated: 6/28/2026, 12:52:17 PM
1class Solution(object):
2    def sortedSquares(self, nums):
3        # x=[]
4        # for num in nums:
5        #     x.append(num*num)
6        # x.sort()
7        # return x
8        for i in range(len(nums)):
9            nums[i]=nums[i]**2
10        nums.sort()
11        return(nums)
12
13        