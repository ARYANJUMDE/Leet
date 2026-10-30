# Last updated: 10/30/2026, 4:23:06 PM
1class Solution(object):
2    def sumOfUnique(self, nums):
3        x={}
4        for i in range(len(nums)):
5            if nums[i] not in x:
6                x[nums[i]]=1
7            else:
8                x[nums[i]]=x[nums[i]]+1
9        x=list(sorted(x.items(),key=lambda x:x[1]))
10        t=0
11        for i in range(len(x)):
12            if x[i][1]==1:
13                t=t+x[i][0]
14            else:
15                break
16        return t
17
18        
19
20
21