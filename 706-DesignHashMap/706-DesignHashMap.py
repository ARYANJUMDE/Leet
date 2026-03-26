# Last updated: 3/26/2026, 10:54:49 AM
1class Solution(object):
2    def groupAnagrams(self, strs):
3        x={}
4        for word in strs:
5            key=''.join(sorted(word))
6            if key not in x:
7                x[key]=[]
8            x[key].append(word)
9        return(list(x.values()))
10
11        