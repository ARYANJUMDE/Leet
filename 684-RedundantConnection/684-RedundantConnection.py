# Last updated: 4/13/2026, 5:58:48 PM
1from collections import deque
2
3class Solution(object):
4    def isBipartite(self, graph):
5        n = len(graph)
6        color = [-1] * n
7        
8        for i in range(n):
9            if color[i] == -1:
10                q = deque([i])
11                color[i] = 0
12                
13                while q:
14                    node = q.popleft()
15                    
16                    for nei in graph[node]:
17                        if color[nei] == -1:
18                            color[nei] = 1 - color[node]
19                            q.append(nei)
20                        elif color[nei] == color[node]:
21                            return False
22        return True