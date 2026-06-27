# Last updated: 6/27/2026, 6:00:51 PM
1class Solution(object):
2    def removeElement(self, nums, val):
3        # i=len(nums)-1
4        # while(i>=0):
5        #     if(nums[i]==val):
6        #         nums.pop(i)
7        #     i=i-1
8        # return(len(nums))
9        # return(nums)
10        x=list(set(nums))
11        for i in range(len(x)):
12            if x[i]==val:
13                while nums.count(x[i])>0:
14                    nums.remove(x[i])
15        return(len(nums))
16
17
18        