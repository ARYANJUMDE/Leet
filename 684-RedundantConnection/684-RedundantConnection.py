# Last updated: 4/13/2026, 5:48:00 PM
1from collections import defaultdict, deque
2
3class Solution(object):
4    def findOrder(self, numCourses, prerequisites):
5        graph = defaultdict(list)
6        indegree = [0] * numCourses
7        
8        
9        for a, b in prerequisites:
10            graph[b].append(a)
11            indegree[a] += 1
12        
13        
14        q = deque()
15        for i in range(numCourses):
16            if indegree[i] == 0:
17                q.append(i)
18        
19        result = []
20        
21        while q:
22            node = q.popleft()
23            result.append(node)
24            
25            for nei in graph[node]:
26                indegree[nei] -= 1
27                if indegree[nei] == 0:
28                    q.append(nei)
29        
30        
31        if len(result) == numCourses:
32            return result
33        else:
34            return []
35        