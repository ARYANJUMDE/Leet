# Last updated: 8/23/2026, 4:07:37 PM
1class Solution(object):
2    def fib(self, n):
3        # if(n==0 or n==1):
4        #     return n
5        # l=[0,1]
6        # for i in range(2,n):
7        #     l.append(l[i-1]+l[i-2])
8        
9        # return l[len(l)-1]+l[len(l)-2]
10        # if n==0:
11        #     return 0
12        # if n==1:
13        #     return 1
14        # dp=[-1]*(n+1)
15        # dp[0]=0
16        # dp[1]=1
17
18        # for i in range(2,len(dp)):
19        #     dp[i]=dp[i-1]+dp[i-2]
20        # return dp[n]
21        if n==0 or n==1:
22            return n
23        dp=[-1]*(n+1)
24        dp[0]=0
25        dp[1]=1
26        for i in range(2,n+1):
27            dp[i]=dp[i-1]+dp[i-2]
28        return dp[n]
29
30
31
32S=Solution()
33S.fib(2)
34        
35        