# Last updated: 9/11/2026, 12:46:40 PM
1
2        
3class Solution(object):
4    def maxSubArray(self, nums):
5        # result=[]
6        # def subarray(a,i):
7        #     if len(a)>0:
8        #         result.append(sum(a))
9        #     if i==len(nums):
10        #         return
11        #     else:
12        #         a.append(nums[i])
13        #         subarray(a,i+1)
14        #         a.pop()
15        #         subarray([],i+1)
16        # subarray([],0)
17        # return max(result)
18        sum1=0
19        max1=nums[0]
20        for i in range(len(nums)):
21            sum1=sum1+nums[i]
22            max1=max(max1,sum1)
23            if sum1<0:
24                sum1=0
25        return max1
26            
27
28        # max_sum = nums[0]
29        # curr_sum = nums[0]
30        
31        # for i in range(1, len(nums)):
32        #     # Either extend the current subarray OR start new from nums[i]
33        #     curr_sum = max(nums[i], curr_sum + nums[i])
34        #     max_sum = max(max_sum, curr_sum)
35        
36        # return max_sum
37
38