# Last updated: 3/16/2026, 8:15:54 PM
1class MyCircularQueue(object):
2
3    def __init__(self, k):
4        self.q = [0] * k
5        self.k = k
6        self.front = 0
7        self.rear = -1
8        self.count = 0
9
10    def enQueue(self, value):
11        if self.isFull():
12            return False
13        
14        self.rear = (self.rear + 1) % self.k
15        self.q[self.rear] = value
16        self.count += 1
17        return True
18
19    def deQueue(self):
20        if self.isEmpty():
21            return False
22        
23        self.front = (self.front + 1) % self.k
24        self.count -= 1
25        return True
26
27    def Front(self):
28        if self.isEmpty():
29            return -1
30        return self.q[self.front]
31
32    def Rear(self):
33        if self.isEmpty():
34            return -1
35        return self.q[self.rear]
36
37    def isEmpty(self):
38        return self.count == 0
39
40    def isFull(self):
41        return self.count == self.k        
42
43
44# Your MyCircularQueue object will be instantiated and called as such:
45# obj = MyCircularQueue(k)
46# param_1 = obj.enQueue(value)
47# param_2 = obj.deQueue()
48# param_3 = obj.Front()
49# param_4 = obj.Rear()
50# param_5 = obj.isEmpty()
51# param_6 = obj.isFull()