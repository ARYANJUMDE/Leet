# Last updated: 12/27/2025, 6:57:13 PM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        a=[]
        num_set=set(nums)
        for i in range(1,len(nums)+1):
            if i not in num_set:
                a.append(i)
        return a

        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         a.append(i)
        # return a
        