# Last updated: 3/16/2026, 8:19:36 PM
1import heapq
2
3class KthLargest(object):
4
5    def __init__(self, k, nums):
6        self.k = k
7        self.heap = nums
8        heapq.heapify(self.heap)
9
10        while len(self.heap) > k:
11            heapq.heappop(self.heap)
12
13    def add(self, val):
14        heapq.heappush(self.heap, val)
15
16        if len(self.heap) > self.k:
17            heapq.heappop(self.heap)
18
19        return self.heap[0]
20
21
22# Your KthLargest object will be instantiated and called as such:
23# obj = KthLargest(k, nums)
24# param_1 = obj.add(val)