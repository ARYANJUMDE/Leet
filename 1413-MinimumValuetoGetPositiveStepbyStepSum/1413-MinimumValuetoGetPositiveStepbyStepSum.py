# Last updated: 7/31/2026, 2:48:06 PM
1class Solution(object):
2    def minStartValue(self, nums):
3        for i in range(1,9999):
4            add=i
5            count=0
6            for j in range(len(nums)):
7                add=add+nums[j]
8                if add<1:
9                    break
10                else:
11                    count=count+1
12            if count==len(nums):
13                return(i)
14
15    