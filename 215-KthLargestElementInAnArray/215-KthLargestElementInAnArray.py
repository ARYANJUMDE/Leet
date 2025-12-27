# Last updated: 12/27/2025, 6:57:51 PM
class Solution(object):
    def findKthLargest(self, nums, k):
        # while k>0:
        #     maxi=nums[0]
        #     for i in range(1,len(nums)):
        #         if(nums[i]>=maxi):
        #             maxi=nums[i]
        #     nums.remove(maxi)
        #     k=k-1
        # return(maxi)
        nums.sort(reverse=True)
        i=0
        
        while(k!=0):
            maxi=nums[i]
            k=k-1
            
            i=i+1
        
        return(maxi)


        