# Last updated: 3/16/2026, 8:17:31 PM
1class MyCircularDeque(object):
2
3    def __init__(self, k):
4        self.k = k
5        self.q = [0] * k
6        self.front = 0
7        self.rear = -1
8        self.count = 0
9
10    def insertFront(self, value):
11        if self.isFull():
12            return False
13        
14        self.front = (self.front - 1) % self.k
15        self.q[self.front] = value
16        self.count += 1
17        
18        if self.count == 1:
19            self.rear = self.front
20            
21        return True
22
23    def insertLast(self, value):
24        if self.isFull():
25            return False
26        
27        self.rear = (self.rear + 1) % self.k
28        self.q[self.rear] = value
29        self.count += 1
30        return True
31
32    def deleteFront(self):
33        if self.isEmpty():
34            return False
35        
36        self.front = (self.front + 1) % self.k
37        self.count -= 1
38        return True
39
40    def deleteLast(self):
41        if self.isEmpty():
42            return False
43        
44        self.rear = (self.rear - 1) % self.k
45        self.count -= 1
46        return True
47
48    def getFront(self):
49        if self.isEmpty():
50            return -1
51        return self.q[self.front]
52
53    def getRear(self):
54        if self.isEmpty():
55            return -1
56        return self.q[self.rear]
57
58    def isEmpty(self):
59        return self.count == 0
60
61    def isFull(self):
62        return self.count == self.k
63
64
65# Your MyCircularDeque object will be instantiated and called as such:
66# obj = MyCircularDeque(k)
67# param_1 = obj.insertFront(value)
68# param_2 = obj.insertLast(value)
69# param_3 = obj.deleteFront()
70# param_4 = obj.deleteLast()
71# param_5 = obj.getFront()
72# param_6 = obj.getRear()
73# param_7 = obj.isEmpty()
74# param_8 = obj.isFull()