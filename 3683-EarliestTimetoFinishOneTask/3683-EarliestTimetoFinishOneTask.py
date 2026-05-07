# Last updated: 5/7/2026, 10:33:06 AM
1class Solution(object):
2    def earliestTime(self, tasks):
3        x=[]
4        for i in range(len(tasks)):
5            x.append(tasks[i][0]+tasks[i][1])
6        return(min(x))