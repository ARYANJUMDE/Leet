# Last updated: 11/7/2026, 11:26:21 AM
1class Solution(object):
2    def trailingZeroes(self, n):
3        n1=1
4        for i in range(1,n+1):
5            n1=n1*i
6        count=0
7        st=str(n1)
8        for i in range(len(st)-1,-1,-1):
9            if st[i]=='0':
10                count=count+1
11            else:
12                break
13        return count