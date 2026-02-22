# Last updated: 2/22/2026, 3:20:20 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        for i in range(0,len(nums)-1):
4            for j in range(i+1,len(nums)):
5                if(nums[i]+nums[j]==target):
6                    return [i,j]
7S=Solution()
8S.twoSum([2,7,11,15],9)
9        