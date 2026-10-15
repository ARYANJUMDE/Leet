# Last updated: 10/15/2026, 4:02:19 PM
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        x=[]
4        for i in range(len(nums)):
5            for j in range(i,len(nums)+1):
6                x.append(len(set(nums[i:j]))**2)
7        return sum(x)
8
9                
10                
11
12