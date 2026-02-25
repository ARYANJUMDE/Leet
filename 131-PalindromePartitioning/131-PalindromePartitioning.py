# Last updated: 2/25/2026, 12:30:19 PM
1class Solution(object):
2    def partition(self, s):
3        res = []
4        
5        def backtrack(start, path):
6            if start == len(s):
7                res.append(path[:])
8                return
9            
10            
11            for end in range(start, len(s)):
12                substring = s[start:end+1]
13                
14            
15                if substring == substring[::-1]:
16                    path.append(substring)      
17                    backtrack(end + 1, path)  
18                    path.pop()               
19        
20        backtrack(0, [])
21        return res
22
23
24        