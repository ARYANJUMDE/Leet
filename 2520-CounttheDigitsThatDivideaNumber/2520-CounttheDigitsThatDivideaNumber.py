# Last updated: 1/26/2026, 11:26:10 AM
1class Solution(object):
2    def countDigits(self, num):
3        x=[]
4        r=str(num)
5        for i in range((len(r))):
6            x.append(int(r[i]))
7        
8        count=0
9        for j in range(len(x)):
10            if(num%x[j]==0):
11                count=count+1
12        return(count)
13        