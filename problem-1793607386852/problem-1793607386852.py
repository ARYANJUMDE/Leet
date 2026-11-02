# Last updated: 11/2/2026, 1:46:26 PM
1class Solution(object):
2    def countMatches(self, items, ruleKey, ruleValue):
3        count=0
4        if ruleKey=="color":
5            for i in range(len(items)):
6                if ruleValue==items[i][1]:
7                    count=count+1
8            return count
9        elif ruleKey=="type":
10            for i in range(len(items)):
11                if ruleValue==items[i][0]:
12                    count=count+1
13            return count
14        else:
15            for i in range(len(items)):
16                if ruleValue==items[i][2]:
17                    count=count+1
18            return count
19        