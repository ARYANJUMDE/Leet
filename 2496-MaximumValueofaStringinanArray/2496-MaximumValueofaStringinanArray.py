# Last updated: 5/15/2026, 11:34:12 AM
1class Solution(object):
2    def maximumValue(self, strs):
3        x=[]
4        for i in range(len(strs)):
5            if strs[i].isdigit():
6                x.append(int(strs[i]))
7            else:
8                
9                x.append(len(strs[i]))
10        return(max(x))
11        