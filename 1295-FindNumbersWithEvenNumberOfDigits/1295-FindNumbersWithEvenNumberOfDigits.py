# Last updated: 9/9/2026, 10:14:24 PM
class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in range(len(nums)):
            if(len(str(nums[i]))%2==0):
                count=count+1
        return(count)
        