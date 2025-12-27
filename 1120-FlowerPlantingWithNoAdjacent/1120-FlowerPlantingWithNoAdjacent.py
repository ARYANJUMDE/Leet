# Last updated: 12/27/2025, 6:56:44 PM
class Solution(object):
    def gardenNoAdj(self, n, paths):
        adj = [[] for _ in range(n)]
        for x, y in paths:
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)
        
        res = [0] * n
        for i in range(n):
            used = {res[j] for j in adj[i] if res[j] != 0}
            for color in range(1, 5):
                if color not in used:
                    
                    res[i] = color
                    break
        return res
        