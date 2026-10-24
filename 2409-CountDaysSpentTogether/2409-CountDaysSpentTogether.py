# Last updated: 10/24/2026, 5:48:49 PM
1class Solution(object):
2    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
3        if leaveAlice<arriveBob or leaveBob<arriveAlice:
4            return(0)
5        else:
6            start=max(arriveAlice,arriveBob)
7            end=min(leaveAlice,leaveBob)
8            months=[31,28,31,30,31,30,31,31,30,31,30,31]
9            return sum(months[:int(end[:2])-1]) + int(end[3:]) - sum(months[:int(start[:2])-1]) - int(start[3:]) + 1
10
11        