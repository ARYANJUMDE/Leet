# Last updated: 7/13/2026, 10:12:53 PM
class Solution(object):
    def searchRange(self, nums, target):
        x=[]
        maxi=len(nums)-1
        mini=0
        while maxi>=mini:
            mid=(maxi+mini)//2
            if(nums[mid]==target):
                x.append(nums.index(target))
                x.append(nums.index(target)+nums.count(target)-1)
                break
            elif(nums[mid]>target):
                maxi=mid-1
            else:
                mini=mid+1
        if(len(x)==0):

            x.append(-1)
            x.append(-1)
        
        return(x)
        