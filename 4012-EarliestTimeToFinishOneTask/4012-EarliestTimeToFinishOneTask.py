# Last updated: 5/18/2026, 12:43:35 PM
class Solution(object):
    def earliestTime(self, tasks):
        x=[]
        for i in range(len(tasks)):
            x.append(tasks[i][0]+tasks[i][1])
        return(min(x))