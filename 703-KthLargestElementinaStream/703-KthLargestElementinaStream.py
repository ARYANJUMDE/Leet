# Last updated: 4/11/2026, 1:11:34 PM
1import heapq
2class KthLargest(object):
3
4    def __init__(self, k, nums):
5        self.k=k
6        self.heap=nums
7
8        heapq.heapify(self.heap)
9        while len(self.heap)>k:
10             heapq.heappop(self.heap)
11
12    def add(self, val):
13        heapq.heappush(self.heap, val)
14        
15        if len(self.heap) > self.k:
16            heapq.heappop(self.heap)
17        
18        return self.heap[0]    
19        
20        
21
22
23# Your KthLargest object will be instantiated and called as such:
24# obj = KthLargest(k, nums)
25# param_1 = obj.add(val)