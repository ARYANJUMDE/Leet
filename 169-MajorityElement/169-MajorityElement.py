# Last updated: 12/27/2025, 6:57:55 PM
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

S=Solution()
S.majorityElement([3,2,3])        