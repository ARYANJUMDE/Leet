# Last updated: 4/13/2026, 5:45:12 PM
1class Solution(object):
2    def findRedundantConnection(self, edges):
3        parent = {}
4
5        def find(x):
6            if parent[x] != x:
7                parent[x] = find(parent[x])  # path compression
8            return parent[x]
9
10        def union(x, y):
11            px = find(x)
12            py = find(y)
13            if px == py:
14                return False  
15            parent[px] = py
16            return True
17
18        
19        for u, v in edges:
20            parent[u] = u
21            parent[v] = v
22
23        
24        for u, v in edges:
25            if not union(u, v):
26                return [u, v]    