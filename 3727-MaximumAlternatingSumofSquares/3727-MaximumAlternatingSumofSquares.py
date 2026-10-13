# Last updated: 10/13/2026, 6:00:59 PM
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        x=[]
4        for i in range(len(nums)):
5            x.append(abs(nums[i]))
6        x.sort(reverse=True)
7        if len(x)%2==0:
8            y=x[:len(x)//2]
9            z=x[len(x)//2:]
10            sum1=0
11            sum2=0
12            for i in range(len(y)):
13                sum1=sum1+y[i]*y[i]
14            for i in range(len(z)):
15                sum2=sum2+z[i]*z[i]
16            return(sum1-sum2)
17        else:
18            y=x[:len(x)//2+1]
19            z=x[len(x)//2+1:]
20            sum1=0
21            sum2=0
22            for i in range(len(y)):
23                sum1=sum1+y[i]*y[i]
24            for i in range(len(z)):
25                sum2=sum2+z[i]*z[i]
26            return(sum1-sum2)
27