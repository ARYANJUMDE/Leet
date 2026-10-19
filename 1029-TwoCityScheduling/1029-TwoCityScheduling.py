# Last updated: 10/19/2026, 10:28:48 PM
1class Solution(object):
2    def twoCitySchedCost(self, costs):
3        costs=sorted(costs,key=lambda x:x[0]-x[1])
4        cost1=0
5        cost2=0
6        for i in range(len(costs)//2):
7            cost1=cost1+costs[i][0]
8        for j in range(len(costs)//2,len(costs)):
9            cost2=cost2+costs[j][1]
10        return cost1+cost2
11        # s1=[]
12        # s2=[]
13        # for i in range(len(costs)):
14        #     s1.append(costs[i][0])
15        #     s2.append(costs[i][1])
16        # cost1=0
17        # cost2=0
18        # while len(s2)!=0:
19        #     t=min(s1)
20        #     p=s1.index(t)
21        #     cost1=cost1+t
22        #     s1.pop(p)
23        #     s2.pop(p)
24        #     z=min(s2)
25        #     q=s2.index(z)
26        #     cost2=cost2+z
27        #     s2.pop(q)
28        #     s1.pop(q)
29        # return cost1+cost2
30
31        