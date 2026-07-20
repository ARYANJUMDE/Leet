# Last updated: 7/20/2026, 8:19:59 PM
1class Solution(object):
2    def hIndex(self, citations):
3        ans=0
4        for i in range(1,len(citations)+1):
5            count=0
6            for j in range(len(citations)):
7                if citations[j]>=i:
8                    count=count+1
9            if count>=i:
10                ans=i
11        
12        return(ans)
13
14        