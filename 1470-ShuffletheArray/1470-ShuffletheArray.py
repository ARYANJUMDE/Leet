# Last updated: 10/27/2026, 6:36:51 PM
1class Solution(object):
2    def shuffle(self, nums, n):
3        x=[]
4        y=[]
5        z=[]
6        for i in range(0,n):
7            x.append(nums[i])
8        for i in range(n,len(nums)):
9            y.append(nums[i])
10        i=0
11        while len(y)>0:
12            if i%2==0:
13                z.append(x[0])
14                x.pop(0)
15            else:
16                z.append(y[0])
17                y.pop(0)
18            i=i+1
19        return z
20