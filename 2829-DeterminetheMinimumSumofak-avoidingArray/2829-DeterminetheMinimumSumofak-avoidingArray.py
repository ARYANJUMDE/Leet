# Last updated: 9/28/2026, 12:45:11 PM
1class Solution(object):
2    def minimumSum(self, n, k):
3        x=set()
4        i=1
5        while len(x)<n:
6            if (k-i) not in x:
7                x.add(i)
8            i=i+1
9        return sum(x)
10        # x=[]
11        # for i in range(1,n+1):
12        #     x.append(i)
13        # new_num=n+1
14        # for i in range(len(x)):
15        #     t=k-x[i]
16        #     if t in x and x.index(t)!=i:
17        #         index=x.index(t)
18        #         if i<index:
19        #             o=x.pop(index)
20        #         else:
21        #             p=x.pop(i)
22        #         x.append(new_num)
23        #         new_num=new_num+1
24        # return sum(x)
25    
26