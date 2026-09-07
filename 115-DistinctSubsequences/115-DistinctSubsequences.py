# Last updated: 9/7/2026, 10:40:55 PM
1class Solution(object):
2    def numDistinct(self, s, t):
3        # result=[0]
4        # def solve(i,y):
5        #     if len(y)>len(t):
6        #         return
7        #     if i==len(s):
8        #         if y==t:
9        #             result[0]=result[0]+1
10        #         return
11        #     else:
12        #         y=y+s[i]
13        #         solve(i+1,y)
14        #         y=y[:-1]
15        #         solve(i+1,y)
16        # solve(0,"")
17        # return result[0]
18
19        dp=[[-1]*len(t) for i in range(len(s))]
20        def solve(i,j,dp):
21            if j<0:
22                return 1
23            if i<0:
24                return 0
25            if dp[i][j]!=-1:
26                return dp[i][j]
27            if t[j]==s[i]:
28                dp[i][j]=solve(i-1,j-1,dp)+solve(i-1,j,dp)
29            if t[j]!=s[i]:
30                dp[i][j]=solve(i-1,j,dp)
31            return dp[i][j]
32        p=solve(len(s)-1,len(t)-1,dp)
33        return(p)
34
35            
36
37
38
39        