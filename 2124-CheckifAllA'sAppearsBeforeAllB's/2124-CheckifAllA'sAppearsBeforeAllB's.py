# Last updated: 11/22/2026, 11:07:09 AM
1class Solution(object):
2    def checkString(self, s):
3        x=[]
4        for i in range(len(s)):
5            if len(x)==0 and s[i]=='a':
6                x.append(i)
7            else:
8                if s[i]=='a':
9                    if i-x[-1]!=1:
10                        return False
11                    else:
12                        x.append(i)
13        if len(x)>0 and x[0]!=0:
14            return False
15        return True