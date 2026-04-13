# Last updated: 4/13/2026, 9:04:17 AM
1class Solution(object):
2    def findCircleNum(self, isConnected):
3        n = len(isConnected)
4        visited = [False] * n
5        
6        def dfs(city):
7            for neighbor in range(n):
8                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
9                    visited[neighbor] = True
10                    dfs(neighbor)
11        
12        provinces = 0
13        
14        for i in range(n):
15            if not visited[i]:
16                visited[i] = True
17                dfs(i)
18                provinces += 1
19        
20        return provinces        