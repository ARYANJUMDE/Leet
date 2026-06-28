# Last updated: 6/28/2026, 4:10:36 PM
1class Solution(object):
2    def reverseWords(self, s):
3        # x=s.split()
4        # x.reverse()
5        # t=""
6        # for i in range(len(x)):
7        #     t=t+x[i]
8        #     if i != len(x) - 1:
9        #         t += " "
10        
11        # return(t)
12        x=s.split()
13        
14        return(' '.join(x[::-1]))
15
16        