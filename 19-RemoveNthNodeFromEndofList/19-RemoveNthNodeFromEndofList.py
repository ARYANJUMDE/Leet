# Last updated: 3/16/2026, 8:12:10 PM
1class Solution(object):
2    def evalRPN(self, tokens):
3        stack = []
4
5        for t in tokens:
6            if t in "+-*/":
7                b = stack.pop()
8                a = stack.pop()
9
10                if t == "+":
11                    stack.append(a + b)
12                elif t == "-":
13                    stack.append(a - b)
14                elif t == "*":
15                    stack.append(a * b)
16                else:   # division
17                    stack.append(int(float(a) / b))   # truncate toward zero
18            else:
19                stack.append(int(t))
20
21        return stack.pop()