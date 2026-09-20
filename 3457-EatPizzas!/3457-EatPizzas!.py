# Last updated: 9/20/2026, 4:04:57 PM
1class Solution(object):
2    def maxWeight(self, pizzas):
3        t=len(pizzas)//4
4        i=1
5        weight=0
6        pizzas.sort()
7        odd=(t+1)//2
8        even=t//2
9        while odd>0:
10            weight=weight+pizzas[-1]
11            pizzas.pop(-1)
12            pizzas.pop(0)
13            pizzas.pop(0)
14            pizzas.pop(0)
15            odd=odd-1
16        while even>0:
17            weight=weight+pizzas[-2]
18            pizzas.pop(-1)
19            pizzas.pop(-1)
20            pizzas.pop(0)
21            pizzas.pop(0)
22            even=even-1
23        return weight
24
25        