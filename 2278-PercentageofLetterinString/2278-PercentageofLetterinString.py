# Last updated: 2/28/2026, 11:53:30 AM
1class Solution(object):
2    def percentageLetter(self, s, letter):
3        count=0
4        for ch in s:
5            if ch==letter:
6                count=count+1
7        t=((count*100//len(s)))
8        return t
9        