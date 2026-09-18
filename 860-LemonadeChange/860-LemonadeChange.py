# Last updated: 9/18/2026, 11:31:54 AM
1class Solution(object):
2    def lemonadeChange(self, bills):
3        five=0
4        ten=0
5        for i in range(len(bills)):
6            if bills[i]==5:
7                five=five+1
8            if bills[i]==10:
9                ten=ten+1
10                if five!=0:
11                    five=five-1
12                else:
13                    return False
14            if bills[i]==20:
15                if five!=0 and ten!=0:
16                    five=five-1
17                    ten=ten-1
18                elif five>=3:
19                    five=five-3
20                else:
21                    return False
22        return True
23
24        