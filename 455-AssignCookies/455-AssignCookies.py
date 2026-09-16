# Last updated: 9/16/2026, 9:38:38 PM
1class Solution(object):
2    def findContentChildren(self, g, s):
3        g.sort()
4        s.sort()
5        count=0
6        l=0
7        r=0
8        while l<len(s) and r<len(g):
9            if s[l]>=g[r]:
10                count=count+1
11                r=r+1
12            l=l+1
13        return count
14        # count=0
15        # for i in range(len(g)):
16        #     for j in range(len(s)):
17        #         if g[i]<=s[j]:
18        #             count=count+1
19        #             s.remove(s[j])
20        #             break
21        
22        
23        # return(count)
24        return count
25
26        