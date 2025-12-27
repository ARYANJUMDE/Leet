# Last updated: 12/27/2025, 6:56:36 PM
class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in range(len(nums)):
            if(len(str(nums[i]))%2==0):
                count=count+1
        return(count)
        