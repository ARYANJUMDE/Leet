# Last updated: 4/11/2026, 2:07:11 PM
1class Solution(object):
2    def partitionLabels(self, s):
3        
4        last = {ch: i for i, ch in enumerate(s)}
5        
6        result = []
7        start = 0
8        end = 0
9        
10        
11        for i, ch in enumerate(s):
12            end = max(end, last[ch])
13            
14        
15            if i == end:
16                result.append(end - start + 1)
17                start = i + 1
18        
19        return result