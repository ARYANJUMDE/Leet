# Last updated: 9/11/2026, 12:48:28 PM
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
22            if max1<sum1:
23                max1=sum1
24            if sum1<0:
25                sum1=0
26        return max1
27            
28
29        # max_sum = nums[0]
30        # curr_sum = nums[0]
31        
32        # for i in range(1, len(nums)):
33        #     # Either extend the current subarray OR start new from nums[i]
34        #     curr_sum = max(nums[i], curr_sum + nums[i])
35        #     max_sum = max(max_sum, curr_sum)
36        
37        # return max_sum
38
39