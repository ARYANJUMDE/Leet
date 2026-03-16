# Last updated: 3/16/2026, 6:57:45 PM
1class MinStack(object):
2
3    def __init__(self):
4        self.stack=[]
5        self.minStack=[]
6
7    def push(self, val):
8        self.stack.append(val)
9        if not self.minStack or val<=self.minStack[-1]:
10            self.minStack.append(val)
11        
12    def pop(self):
13
14        if self.minStack[-1]==self.stack[-1]:
15            self.minStack.pop()
16        self.stack.pop()
17        
18
19    def top(self):
20        return self.stack[-1]
21        
22
23    def getMin(self):
24        return self.minStack[-1]
25        
26
27
28# Your MinStack object will be instantiated and called as such:
29# obj = MinStack()
30# obj.push(val)
31# obj.pop()
32# param_3 = obj.top()
33# param_4 = obj.getMin()