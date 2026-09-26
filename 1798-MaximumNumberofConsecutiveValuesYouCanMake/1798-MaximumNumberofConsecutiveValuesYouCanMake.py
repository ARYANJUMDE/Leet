# Last updated: 9/26/2026, 6:54:45 PM
1class Solution(object):
2    def getMaximumConsecutive(self, coins):
3        # reach=0
4        # coins.sort()
5        # for i in range(len(coins)):
6        #     if coins[i]>reach+1:
7        #         break
8        #     reach=reach+coins[i]
9        # return reach+1
10        coins.sort()
11        # a=[0]
12        # s=set()
13        # for i in range(len(coins)):
14        #     for j in range(len(a)):
15        #         t=a[j]+coins[i]
16        #         if t not in s:
17        #             a.append(t)
18        #             s.add(t)
19        #         if a[-2]!=a[-1]-1:
20        #             a.pop()
21        #             break
22        # return(len(a))
23        coins.sort()
24        max_val=0
25        for i in range(len(coins)):
26            if max_val+1<coins[i]:
27                break
28            max_val=max_val+coins[i]
29        return max_val+1
30                    