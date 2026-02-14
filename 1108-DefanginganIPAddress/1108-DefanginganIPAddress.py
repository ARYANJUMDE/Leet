# Last updated: 2/14/2026, 11:05:28 AM
1class Solution(object):
2    def defangIPaddr(self, address):
3        x=''
4        for ch in address:
5            if ch=='.':
6                x=x+'[.]'
7            else:
8                x=x+ch
9        return(x)
10        