# Last updated: 12/27/2025, 6:58:03 PM
class Solution(object):
    def singleNumber(self, nums):
        # for i in range(0,len(nums)):
        #     if nums.count(nums[i])==1:
        #         return (nums[i])
        for num in nums:
            if nums.count(num)==1:
                return (num)


        