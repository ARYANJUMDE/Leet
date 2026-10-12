# Last updated: 10/12/2026, 10:14:52 PM
1class Solution:
2    def lastStoneWeight(self, stones: list[int]) -> int:
3        stones.sort()
4        x=len(stones)
5        while x>1:
6            if stones[-1]==stones[-2]:
7                stones.pop(-1)
8                stones.pop(-1)
9                stones.sort()
10            else:
11                x=stones[-1]-stones[-2]
12                stones.pop(-1)
13                stones.pop(-1)
14                stones.append(x)
15                stones.sort()
16            x=len(stones)
17        
18        if len(stones)==0:
19            return 0
20        return stones[0]
21
22    