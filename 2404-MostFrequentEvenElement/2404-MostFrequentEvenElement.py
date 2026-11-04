# Last updated: 11/4/2026, 3:22:39 PM
1class Solution(object):
2    def mostFrequentEven(self, nums):
3        x={}
4        for i in range(len(nums)):
5            if nums[i]%2==0:
6                if nums[i] not in x:
7                    x[nums[i]]=1
8                else:
9                    x[nums[i]]=x[nums[i]]+1
10        if len(x)>0:
11            x=sorted(x.items(),key=lambda x:(x[1],-x[0]),reverse=True)
12            return x[0][0]
13        return -1
14        
15