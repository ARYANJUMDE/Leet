# Last updated: 12/27/2025, 6:57:50 PM
class Solution(object):
    def rotate(self, nums, k):
        # for i in range(0,k):
        #     x=nums[len(nums)-1]
        #     for j in range(len(nums)-1,0,-1):
        #         nums[j]=nums[j-1]###right rotation
        #     nums[0]=x
        # for i in range(k):
        #     nums.insert(0,nums[-1])
        #     del nums[-1]
        # return(nums) 
        k=k%len(nums)    
        nums[:] = nums[-k:] + nums[:-k]