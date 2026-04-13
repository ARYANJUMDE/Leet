# Last updated: 4/13/2026, 5:57:40 PM
1import heapq
2
3class Solution(object):
4    def minCostConnectPoints(self, points):
5        n = len(points)
6        visited = set()
7        heap = [(0, 0)]  # (cost, point_index)
8        total_cost = 0
9        
10        while len(visited) < n:
11            cost, i = heapq.heappop(heap)
12            
13            if i in visited:
14                continue
15            
16            visited.add(i)
17            total_cost += cost
18            
19            for j in range(n):
20                if j not in visited:
21                    x1, y1 = points[i]
22                    x2, y2 = points[j]
23                    dist = abs(x1 - x2) + abs(y1 - y2)
24                    heapq.heappush(heap, (dist, j))
25        
26        return total_cost
27        