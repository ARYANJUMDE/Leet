# Last updated: 8/28/2026, 3:21:18 PM
1class Solution(object):
2    def rob(self, nums):
3        # dp=[-1]*len(nums)
4        # def robbing(i):
5        #     if i>=len(nums):
6        #         return 0
7        #     if dp[i]!=-1:
8        #         return dp[i]
9        #     take=nums[i]+robbing(i+2)
10        #     skip=robbing(i+1)
11        #     dp[i]=max(take,skip)
12        #     return dp[i]
13        # return robbing(0)
14        dp=[-1]*len(nums)
15        def robbing(i):
16            if i>=len(nums):
17                return 0
18            if dp[i]!=-1:
19                return dp[i]
20            else:
21                take=nums[i]+robbing(i+2)
22                skip=robbing(i+1)
23                dp[i]=max(take,skip)
24                return dp[i]
25        return robbing(0)
26        # # dp=[-1]*len(nums)
27        # for i in range(len(nums)):
28        
29        # Normal recusion code
30        # x=[]
31        # def robbing(sum1,i):
32        #     if i>=len(nums):
33        #         x.append(sum1)
34        #         return
35        #     else:
36        #         sum1=sum1+nums[i]
37        #         robbing(sum1,i+2)
38        #         sum1=sum1-nums[i]
39        #         robbing(sum1,i+1)
40        # t=robbing(0,0)
41        # return (max(x))    
42
43        # prev1 = 0
44        # prev2 = 0
45        
46        # for num in nums:
47        #     temp = max(prev1, prev2 + num)
48        #     prev2 = prev1
49        #     prev1 = temp
50        
51        # return prev1