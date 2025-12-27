# Last updated: 12/27/2025, 6:58:12 PM

        
class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the current subarray OR start new from nums[i]
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

S = Solution()
print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
