# Last updated: 4/21/2026, 12:01:05 PM
1class Solution(object):
2    def sortPeople(self, names, heights):
3        x=[]
4        for i in range (len(names)):
5            x.append([names[i],heights[i]])
6        x.sort(key=lambda t:t[1],reverse=True)
7        y=[]
8        for i in range(len(x)):
9            y.append(x[i][0])
10        
11        
12        return(y)
13
14
15        