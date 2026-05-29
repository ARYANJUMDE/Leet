# Last updated: 5/29/2026, 11:06:04 AM
1class Solution(object):
2    def minElement(self, nums):
3        x=[]
4        for i in range(len(nums)):
5            s=0
6            while nums[i]>0:
7                t=nums[i]%10
8                s=s+t
9                nums[i]=nums[i]//10
10            x.append(s)
11        
12        return(min(x))
13        
14    
15
16        