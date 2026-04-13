# Last updated: 4/13/2026, 9:06:56 AM
1import heapq
2from collections import Counter
3class Solution(object):
4    def reorganizeString(self, s):
5        freq = Counter(s)
6        
7        maxHeap = []
8        for ch in freq:
9            heapq.heappush(maxHeap, (-freq[ch], ch))
10        
11        prev = (0, '')
12        result = ""
13        
14        while maxHeap:
15            count, ch = heapq.heappop(maxHeap)
16            result += ch
17            
18            if prev[0] < 0:
19                heapq.heappush(maxHeap, prev)
20            
21            count += 1  
22            prev = (count, ch)
23        
24        if len(result) != len(s):
25            return ""
26        
27        return result        