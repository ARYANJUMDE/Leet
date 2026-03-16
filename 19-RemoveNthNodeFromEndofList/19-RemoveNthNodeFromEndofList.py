# Last updated: 3/16/2026, 8:47:37 PM
1class Solution(object):
2    def dailyTemperatures(self, temperatures):
3        n = len(temperatures)
4        answer = [0]*n
5        stack = []
6
7        for i in range(n):
8            
9            while stack and temperatures[i] > temperatures[stack[-1]]:
10                prev = stack.pop()
11                answer[prev] = i - prev
12            
13            stack.append(i)
14
15        return answer