# Last updated: 5/20/2026, 11:46:01 AM
1class Solution(object):
2    def countBinarySubstrings(self, s):
3        
4        prev = 0
5        curr = 1
6        count = 0
7        
8        for i in range(1, len(s)):
9            
10            if s[i] == s[i-1]:
11                curr += 1
12            else:
13                count += min(prev, curr)
14                prev = curr
15                curr = 1
16        
17        count += min(prev, curr)
18        
19        return count