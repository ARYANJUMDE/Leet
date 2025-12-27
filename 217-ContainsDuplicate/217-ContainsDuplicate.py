# Last updated: 12/27/2025, 6:57:49 PM
class Solution(object):
    def containsDuplicate(self, nums):
        # for num in nums:
        #     if(nums.count(num)>=2):
        #         return True
        # return False
        #or
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        #or
        return len(nums) != len(set(nums))
S=Solution()
S.containsDuplicate([1,2,3,1])

        