# Last updated: 11/24/2026, 11:19:13 AM
1class Solution:
2    def maxLength(self, nums: List[int]) -> int:
3        from math import gcd,lcm
4        max_len=float('-inf')
5        for i in range(len(nums)):
6            prod=1
7            x=[]
8            for j in range(i,len(nums)):
9                prod=prod*nums[j]
10                x.append(nums[j])
11                g=math.gcd(*x)
12                l=math.lcm(*x)
13                if prod==g*l:
14                    if j-i+1>max_len:
15                        max_len=j-i+1
16        return max_len
17
18
19        