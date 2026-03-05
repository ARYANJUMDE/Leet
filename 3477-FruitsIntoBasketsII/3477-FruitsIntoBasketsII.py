# Last updated: 3/5/2026, 10:55:41 AM
1class Solution(object):
2    def numOfUnplacedFruits(self, fruits, baskets):
3        x=[]
4        for i in range(len(fruits)):
5            for j in range(len(baskets)):
6                if(baskets[j]>=fruits[i]):
7                    x.append(fruits[i])
8                    baskets.pop(j)
9                    break
10        
11        return(len(fruits)-len(x))
12
13        