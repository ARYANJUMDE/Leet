# Last updated: 12/27/2025, 6:56:52 PM
class Solution(object):
    def search(self, nums, target):
        maxi=len(nums)-1
        mini=0
        while mini<=maxi:
            mid=(maxi+mini)//2
            
            if(nums[mid]==target):
                return mid
            elif(target>nums[mid]):
                mini=mid+1
            else:
                
                maxi=mid-1
        else:
            return -1
    
        