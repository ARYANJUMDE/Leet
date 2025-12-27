# Last updated: 12/27/2025, 6:58:01 PM
class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if(nums.count(num)==1):
                return(num)
                break
        