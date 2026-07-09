# Last updated: 7/9/2026, 4:17:12 PM
1class Solution(object):
2    def numberOfMatches(self, n):
3        count=0
4        while n!=1:
5            if n%2==0:
6                count=count+n/2
7                n=n/2
8            if n%2!=0:
9                count=count+(n-1)/2
10                n=((n-1)/2)+1
11        
12        return(int(count))
13        