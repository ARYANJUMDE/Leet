# Last updated: 9/22/2026, 6:03:41 PM
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
18        # sum1=0
19        # max1=nums[0]
20        # for i in range(len(nums)):
21        #     sum1=sum1+nums[i]
22        #     if max1<sum1:
23        #         max1=sum1
24        #     if sum1<0:
25        #         sum1=0
26        # return max1
27        
28            
29
30        # max_sum = nums[0]
31        # curr_sum = nums[0]
32        
33        # for i in range(1, len(nums)):
34        #     # Either extend the current subarray OR start new from nums[i]
35        #     curr_sum = max(nums[i], curr_sum + nums[i])
36        #     max_sum = max(max_sum, curr_sum)
37        
38        # return max_sum
39
40
41        i=0
42        j=0
43        sum1=0
44        max_sum=float('-inf')
45        while j<len(nums):
46            if sum1>=0:
47                sum1=sum1+nums[j]
48                if sum1>max_sum:
49                    max_sum=sum1
50                j=j+1
51            else:
52                while sum1<0:
53                    sum1=sum1-nums[i]
54                    i=i+1
55                    if sum1>max_sum:
56                        max_sum=sum1
57        if max_sum==0:
58            if 0 in nums:
59                return max_sum
60        if max_sum==0:
61            if 0 not in nums:
62                return max(nums)
63        return max_sum
64        
65
66                    
67    
68
69
70