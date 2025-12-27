# Last updated: 12/27/2025, 6:56:15 PM
class Solution(object):
    def minimumRightShifts(self, nums):
        # count=0
        # while nums!=sorted(nums):
        #     first=nums[0]
        #     last=nums[-1]
        #     nums.remove(first)
        #     nums.insert(0,last)
        #     nums.pop()
        #     nums.insert(1,first)
        #     count=count+1
        #     if(count>len(nums)):
        #         count=-1
        #         break
        # return(count)


        if nums==sorted(nums):
            return 0
        for k in range(0,len(nums)):
            rotated=nums[-k:]+nums[:-k]
            if rotated==sorted(nums):
                return k

        return -1

    
        