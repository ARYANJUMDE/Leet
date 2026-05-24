# Last updated: 5/24/2026, 11:29:20 AM
1class Solution(object):
2    def getMaximumGenerated(self, n):
3        if n==0:
4            return 0
5        nums=[0,1]
6        while len(nums)<n+1:
7            for i in range(1,n+1):
8                if 2*i%2==0 and len(nums)<n+1:
9                    nums.append(nums[i])
10                
11                if (2*i+1)%2!=0 and len(nums)<n+1:
12                    nums.append(nums[i]+nums[i+1])
13        return(max(nums))
14        
15
16        