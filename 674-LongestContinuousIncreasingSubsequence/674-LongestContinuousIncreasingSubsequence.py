# Last updated: 2/16/2026, 3:37:21 PM
1class Solution(object):
2    def findLengthOfLCIS(self, nums):
3        # count=0
4        # for i in range(len(nums)-1):
5        #     if(nums[i]<nums[i+1]):
6        #         count=count+1
7        # if(count==0):
8        #     return(1)
9        # else:
10        #     return(count)
11        max_len=1
12        curr_len=1
13        
14        for i in range(len(nums)-1):
15            if(nums[i]<nums[i+1]):
16                curr_len=curr_len+1
17                
18                max_len=max(max_len,curr_len)
19            else:
20                curr_len=1
21        return(max_len)
22        