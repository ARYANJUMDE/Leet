# Last updated: 11/8/2026, 10:59:11 AM
1class Solution(object):
2    def alternateDigitSum(self, n):
3        st=str(n)
4        x=[]
5        for i in range(len(st)):
6            if i%2!=0:
7                x.append(int("-"+st[i]))
8            else:
9                x.append(int(st[i]))
10        return(sum(x))
11        