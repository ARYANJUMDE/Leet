# Last updated: 9/9/2026, 10:10:58 PM
from fractions import gcd
class Solution(object):
    def countPairs(self, nums, k):
        count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if((nums[i]*nums[j])%k==0):
        #             count=count+1
        mp={}
        for num in nums:
            g=gcd(num,k)
            for prev in mp:
                if(g*prev)%k==0:
                    count=count+mp[prev]
            mp[g]=mp.get(g,0)+1
        

        return count

        