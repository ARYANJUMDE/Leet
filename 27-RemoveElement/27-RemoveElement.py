# Last updated: 12/28/2025, 12:34:49 PM
1class Solution(object):
2    def removeElement(self, nums, val):
3        i=len(nums)-1
4        while(i>=0):
5            if(nums[i]==val):
6                nums.pop(i)
7            i=i-1
8        return(len(nums))
9        return(nums)
10
11        