# Last updated: 3/3/2026, 11:22:05 AM
1class Solution(object):
2    def findRelativeRanks(self, score):
3        x=[]
4        y=sorted(score)
5        t=sorted(score,reverse=True)
6        for i in range(len(score)):
7            if(score[i] not in x):
8                if(score[i]==max(score)):
9                    x.append('Gold Medal')
10                elif(score[i]==y[-2]):
11                    x.append('Silver Medal')
12                elif(score[i]==y[-3]):
13                    x.append('Bronze Medal')
14                else:
15                    x.append(str(t.index(score[i])+1))
16        return(x)
17
18        