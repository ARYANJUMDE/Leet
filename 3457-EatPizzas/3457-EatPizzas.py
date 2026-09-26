# Last updated: 9/26/2026, 4:14:49 PM
class Solution(object):
    def maxWeight(self, pizzas):
        t=len(pizzas)//4
        i=1
        weight=0
        pizzas.sort()
        odd=(t+1)//2
        even=t//2
        while odd>0:
            weight=weight+pizzas[-1]
            pizzas.pop(-1)
            pizzas.pop(0)
            pizzas.pop(0)
            pizzas.pop(0)
            odd=odd-1
        while even>0:
            weight=weight+pizzas[-2]
            pizzas.pop(-1)
            pizzas.pop(-1)
            pizzas.pop(0)
            pizzas.pop(0)
            even=even-1
        return weight

        