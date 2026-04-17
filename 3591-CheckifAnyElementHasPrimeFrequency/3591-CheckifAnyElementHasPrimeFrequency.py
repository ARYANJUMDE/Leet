# Last updated: 4/17/2026, 10:07:39 AM
1class Solution(object):
2    def checkPrimeFrequency(self, nums):
3        x=[]
4        for num in nums:
5            if num not in x:
6                x.append(num)
7        y=[]
8        for num in x:
9            y.append(nums.count(num))
10        for i in range(len(y)):
11            count=0
12            for j in range(1,y[i]+1):
13                if y[i]%j==0:
14                    count=count+1
15            if count==2:
16                return(True)
17        else:
18            return(False)
19
20        