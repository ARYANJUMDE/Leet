# Last updated: 12/27/2025, 6:57:00 PM
class Solution(object):
    def maximumProduct(self, nums):

        nums.sort(reverse=True)
        case1=(nums[0]*nums[1]*nums[2])
        case2=(nums[0]*nums[-1]*nums[-2])
        return max(case1,case2)
        