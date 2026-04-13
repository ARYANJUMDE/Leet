# Last updated: 4/13/2026, 5:56:26 PM
1import heapq
2from collections import defaultdict
3
4class Solution(object):
5    def networkDelayTime(self, times, n, k):
6        graph = defaultdict(list)
7        
8        
9        for u, v, w in times:
10            graph[u].append((v, w))
11        
12        
13        heap = [(0, k)]
14        visited = set()
15        max_time = 0
16        
17        while heap:
18            time, node = heapq.heappop(heap)
19            
20            if node in visited:
21                continue
22            
23            visited.add(node)
24            max_time = max(max_time, time)
25            
26            for nei, wt in graph[node]:
27                if nei not in visited:
28                    heapq.heappush(heap, (time + wt, nei))
29        
30        
31        return max_time if len(visited) == n else -1