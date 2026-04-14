# Last updated: 4/14/2026, 10:09:32 AM
1class Solution(object):
2    def numOfStrings(self, patterns, word):
3        count=0
4        for ch in patterns:
5            if ch in word:
6                count=count+1
7        
8        
9        return(count)
10        