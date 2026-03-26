# Last updated: 3/26/2026, 10:45:39 AM
1class MyHashMap:
2
3    def __init__(self):
4        self.map = [-1] * 1000001   
5
6    def put(self, key, value):
7        self.map[key] = value
8
9    def get(self, key):
10        return self.map[key]
11
12    def remove(self, key):
13        self.map[key] = -1
14
15
16# Your MyHashMap object will be instantiated and called as such:
17# obj = MyHashMap()
18# obj.put(key,value)
19# param_2 = obj.get(key)
20# obj.remove(key)