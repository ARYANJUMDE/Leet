# Last updated: 9/23/2026, 5:23:14 PM
1class Solution(object):
2    def maximumNumber(self, num, change):
3        x=[]
4        y=[]
5        for i in range(len(num)):
6            x.append(int(num[i]))
7        for i in range(len(num)):
8            y.append(change[int(num[i])])
9        z=[]
10        for i in range(len(x)):
11            if x[i]<y[i]:
12                z.append(i)
13        if len(z)>0:
14            start=z[0]
15            for i in range(start,len(x)):
16                if x[i]<=y[i]:
17                    x[i]=y[i]
18                else:
19                    break
20        t=""
21        for i in range(len(x)):
22            t=t+str(x[i])
23        return t
24
25        # x=[]
26        # y=[]
27        # for i in range(len(num)):
28        #     x.append(change[int(num[i])])
29        # for i in range(len(num)):
30        #     y.append(int(num[i]))
31        # i=0
32        # j=0
33        # z=[]
34        # while j<len(x):
35        #     if x[j]>y[j]:
36        #         j=j+1
37        #     else:
38        #         if i!=j:
39        #             z.append([i,j-1])
40        #         j=j+1
41        #         while i!=j:
42        #             i=i+1
43        # z.append([i,j-1])
44        # if len(z)>0:
45        #     for i in range(z[0][0],z[0][1]+1):
46        #         y[i]=x[i]
47        # st=""
48        # for i in range(len(y)):
49        #     st=st+str(y[i])
50        # return(st)
51
52        