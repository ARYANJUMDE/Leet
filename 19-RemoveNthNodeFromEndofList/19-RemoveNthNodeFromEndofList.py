# Last updated: 3/16/2026, 6:48:36 PM
1from  collections import deque
2class MyStack(object):
3
4    def __init__(self):
5        self.q1=deque()
6        self.q2=deque()
7
8    def push(self, x):
9        self.q2.append(x)
10        while self.q1:
11            self.q2.append(self.q1.popleft())
12        self.q1,self.q2=self.q2,self.q1
13
14    def pop(self):
15        return self.q1.popleft()
16    def top(self):
17
18        return self.q1[0]
19    def empty(self):
20        return len(self.q1)==0
21        
22# Your MyStack object will be instantiated and called as such:
23# obj = MyStack()
24# obj.push(x)
25# param_2 = obj.pop()
26# param_3 = obj.top()
27# param_4 = obj.empty()