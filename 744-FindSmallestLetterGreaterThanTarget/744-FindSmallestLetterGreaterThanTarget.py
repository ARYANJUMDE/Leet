# Last updated: 1/31/2026, 12:11:51 PM
1class Solution(object):
2    def nextGreatestLetter(self, letters, target):
3        x=[]
4        for i in range(len(letters)):
5            x.append(letters[i])
6        heapq.heapify(letters)
7        while len(letters)>0:
8            if letters[0]>target:
9                return(letters[0])
10
11            else:
12                heapq.heappop(letters)
13        return x[0]
14        