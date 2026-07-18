# Last updated: 7/18/2026, 8:52:22 PM
1class Solution(object):
2    def reconstructQueue(self, people):
3        people=sorted(people,key=lambda x:(-x[0],x[1]))
4        x=[]
5        for i in range (len(people)):
6            x.insert(people[i][1],people[i])
7        
8        
9        return(x)
10        