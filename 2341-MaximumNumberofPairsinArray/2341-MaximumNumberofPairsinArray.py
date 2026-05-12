# Last updated: 5/12/2026, 11:36:36 AM
1class Solution(object):
2    def numberOfPairs(self, nums):
3        x=[]
4        for num in nums:
5            if num not in x:
6                x.append(num)
7        y=[]
8        for num in x:
9            y.append(nums.count(num))
10        count=0
11        z=0
12        for i in range(len(y)):
13            
14            if y[i]%2==0:
15                count=count+y[i]//2
16            else:
17                
18                count=count+(y[i]-1)//2
19                z=z+1
20        t=[count,z]
21        return(t)
22
23        