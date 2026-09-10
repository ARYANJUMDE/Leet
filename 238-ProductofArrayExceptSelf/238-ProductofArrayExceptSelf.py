# Last updated: 9/10/2026, 10:47:31 AM
1class Solution(object):
2    def productExceptSelf(self, nums):
3        if 0 not in nums:
4            t=1
5            x=[]
6            for i in range(len(nums)):
7                t=t*nums[i]
8            for i in range(len(nums)):
9                x.append(t//nums[i])
10            return x
11        else:
12            t=1
13            count=0
14            y=[]
15            for i in range(len(nums)):
16                if nums[i]!=0:
17                    t=t*nums[i]
18                else:
19                    count=count+1
20            if count==1:
21                for i in range(len(nums)):
22                    if nums[i]==0:
23                        y.append(t)
24                    else:
25                        y.append(0)
26            else:
27                y=[0]*len(nums)
28                
29            return y
30
31            
32        # import math
33        # x=[]
34        # for i in range(0,len(nums)):
35        #     t=nums.pop(nums[i])
36        #     y=math.prod(nums)
37        #     x.append(y)
38        # nums.insert(i,t)
39        
40        
41        # return(x)
42
43        