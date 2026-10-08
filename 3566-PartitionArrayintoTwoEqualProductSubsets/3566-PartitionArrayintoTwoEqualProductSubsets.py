# Last updated: 10/8/2026, 10:51:50 PM
1class Solution(object):
2    def checkEqualPartitions(self, nums, target):
3        count=[0]
4        y=[]
5        def solve(i,x):
6            if i>len(nums) or count[0]==1:
7                return
8            if i==len(nums):
9                t=1
10                for i in range(len(x)):
11                    t=t*x[i]
12                if t==target:
13                    count[0]=count[0]+1
14                    for i in range(len(x)):
15                        y.append(x[i])
16                return
17            x.append(nums[i])
18            solve(i+1,x)
19            x.pop()
20            solve(i+1,x)
21        solve(0,[])
22        if count[0]==1:
23            for i in range(len(y)):
24                nums.remove(y[i])
25            z=1
26            for i in range(len(nums)):
27                z=z*nums[i]
28            if z==target:
29                return True
30        return False
31        