# Last updated: 11/6/2026, 1:20:54 PM
1class Solution(object):
2    def numberOfEmployeesWhoMetTarget(self, hours, target):
3        count=0
4        for i in range(len(hours)):
5            if hours[i]>=target:
6                count=count+1
7        return count
8        