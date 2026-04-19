# Last updated: 4/19/2026, 10:17:26 AM
1class Solution(object):
2    def isArraySpecial(self, nums):
3        if(len(nums)==1):
4            return(True)
5        else:
6            for i in range(len(nums)-1):
7                if (nums[i]%2==0 and nums[i+1]%2==0) or (nums[i]%2!=0 and nums[i+1]%2!=0):
8                    return(False)
9            else:
10                return(True)
11            
12
13        