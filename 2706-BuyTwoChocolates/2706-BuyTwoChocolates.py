# Last updated: 11/25/2026, 11:03:57 AM
1class Solution:
2    def buyChoco(self, prices: List[int], money: int) -> int:
3        prices.sort()
4        count=0
5        x=money
6        for i in range(len(prices)):
7            t=money-prices[i]
8            if t>=0 and count!=2:
9                money=money-prices[i]
10                count=count+1
11            else:
12                break
13        if count==2 and money>=0:
14            return money
15        return x
16