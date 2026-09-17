# Last updated: 9/17/2026, 6:35:30 PM
1class Solution(object):
2    def minSumOfLengths(self, arr, target):
3        r=0
4        l=0
5        sum1=0
6        count=0
7        x=[]
8        while r<len(arr):
9            sum1=arr[r]+sum1
10            if sum1==target:
11                x.append([r-l+1,l,r])
12            if sum1>target:
13                while sum1>target:
14                    sum1=sum1-arr[l]
15                    l=l+1
16                    if sum1==target:
17                        x.append([r-l+1,l,r])
18            r=r+1
19        if len(x)<2:
20            return -1
21        else:
22            x.sort(key=lambda t: t[2])
23            ans = float('inf')
24            min_len = float('inf')
25            j = 0
26            for i in range(len(x)):
27                while j < len(x) and x[j][2] < x[i][1]:
28                    min_len = min(min_len, x[j][0])
29                    j = j + 1
30                if min_len != float('inf'):
31                    ans = min(ans, min_len + x[i][0])
32            if ans == float('inf'):
33                 return -1
34            return ans
35                
36
37
38