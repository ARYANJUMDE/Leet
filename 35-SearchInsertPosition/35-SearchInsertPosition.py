# Last updated: 12/27/2025, 6:58:17 PM
class Solution(object):
    def searchInsert(self, nums, target):
        maxi=len(nums)-1
        mini=0
        while(mini<=maxi):
            mid=(maxi+mini)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                maxi=mid-1
            else:
                mini=mid+1          
        
        return mini
        