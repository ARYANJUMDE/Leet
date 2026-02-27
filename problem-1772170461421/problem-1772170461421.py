# Last updated: 2/27/2026, 11:04:21 AM
1class Solution(object):
2    def searchRange(self, nums, target):
3        x=[]
4        maxi=len(nums)-1
5        mini=0
6        while maxi>=mini:
7            mid=(maxi+mini)//2
8            if(nums[mid]==target):
9                x.append(nums.index(target))
10                x.append(nums.index(target)+nums.count(target)-1)
11                break
12            elif(nums[mid]>target):
13                maxi=mid-1
14            else:
15                mini=mid+1
16        if(len(x)==0):
17
18            x.append(-1)
19            x.append(-1)
20        
21        return(x)
22        