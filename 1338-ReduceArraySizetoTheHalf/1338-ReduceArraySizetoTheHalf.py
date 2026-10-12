# Last updated: 10/12/2026, 1:17:50 PM
1class Solution:
2    def minSetSize(self, arr: list[int]) -> int:
3        x={}
4        t=len(arr)//2
5        for i in range(len(arr)):
6            if arr[i] not in x:
7                x[arr[i]]=1
8            else:
9                x[arr[i]]=x[arr[i]]+1
10        x=dict(sorted(x.items(),key=lambda x:x[1],reverse=True))
11        count=0
12        sum1=0
13        for ch in x:
14            sum1=sum1+x[ch]
15            count=count+1
16            if sum1>=(t):
17                break
18        return(count)
19
20        