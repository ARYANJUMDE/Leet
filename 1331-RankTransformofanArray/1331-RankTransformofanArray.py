# Last updated: 10/4/2026, 1:10:28 PM
1class Solution(object):
2    def arrayRankTransform(self, arr):
3        x=list(set(arr))
4        x.sort()
5        y={}
6        for i in range(len(x)):
7            if x[i] not in y:
8                y[x[i]]=i+1
9        z=[]
10        for i in range(len(arr)):
11            z.append(y[arr[i]])
12        return(z)
13        # y=[]
14        # for i in range(len(arr)):
15        #     y.append(x.index(arr[i])+1)
16        # return(y)
17        # # x=[]
18        # y=[]
19        # for i in range(len(arr)):
20        #     x.append(arr[i])
21        # t=[]
22        # for i in range(len(arr)):
23        #     if arr[i] not in t:
24        #         t.append(arr[i])
25        # t.sort()
26        # for i in range(len(x)):
27        #     y.append(t.index(x[i])+1)
28        # return y