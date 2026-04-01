# Last updated: 4/1/2026, 4:37:55 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0]*n
        stack = []

        for i in range(n):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            
            stack.append(i)

        return answer