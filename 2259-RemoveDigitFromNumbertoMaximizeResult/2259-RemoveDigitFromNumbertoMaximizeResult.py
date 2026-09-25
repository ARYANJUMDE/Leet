# Last updated: 9/25/2026, 9:55:29 PM
1class Solution(object):
2    def removeDigit(self, number, digit):
3        x=[]
4        y=[]
5        for i in range(len(number)):
6            if number[i]==digit:
7                x.append(i)
8        for i in range(len(x)):
9            y.append(int(number[:x[i]]+""+number[x[i]+1:]))
10        return str((max(y)))
11
12        