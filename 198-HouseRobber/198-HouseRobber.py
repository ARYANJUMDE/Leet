# Last updated: 8/27/2026, 9:57:41 PM
1class Solution(object):
2    def rob(self, nums):
3        dp=[-1]*len(nums)
4        def robbing(i):
5            if i>=len(nums):
6                return 0
7            if dp[i]!=-1:
8                return dp[i]
9            take=nums[i]+robbing(i+2)
10            skip=robbing(i+1)
11            dp[i]=max(take,skip)
12            return dp[i]
13        return robbing(0)
14        # dp=[-1]*len(nums)
15        # for i in range(len(nums)):
16        
17        # Normal recusion code
18        # x=[]
19        # def robbing(sum1,i):
20        #     if i>=len(nums):
21        #         x.append(sum1)
22        #         return
23        #     else:
24        #         sum1=sum1+nums[i]
25        #         robbing(sum1,i+2)
26        #         sum1=sum1-nums[i]
27        #         robbing(sum1,i+1)
28        # t=robbing(0,0)
29        # return (max(x))    
30
31        # prev1 = 0
32        # prev2 = 0
33        
34        # for num in nums:
35        #     temp = max(prev1, prev2 + num)
36        #     prev2 = prev1
37        #     prev1 = temp
38        
39        # return prev1