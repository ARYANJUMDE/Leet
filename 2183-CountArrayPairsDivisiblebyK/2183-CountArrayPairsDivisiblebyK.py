# Last updated: 1/25/2026, 12:17:27 PM
1from fractions import gcd
2class Solution(object):
3    def countPairs(self, nums, k):
4        count=0
5        # for i in range(len(nums)):
6        #     for j in range(i+1,len(nums)):
7        #         if((nums[i]*nums[j])%k==0):
8        #             count=count+1
9        mp={}
10        for num in nums:
11            g=gcd(num,k)
12            for prev in mp:
13                if(g*prev)%k==0:
14                    count=count+mp[prev]
15            mp[g]=mp.get(g,0)+1
16        
17
18        return count
19
20        