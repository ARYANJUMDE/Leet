# Last updated: 7/21/2026, 11:33:45 AM
1class Solution(object):
2    def numRescueBoats(self, people, limit):
3        people.sort()
4        i=0
5        j=len(people)-1
6        count=0
7        while i<=j:
8            if people[i]+people[j]<=limit:
9                count=count+1
10                i=i+1
11                j=j-1
12            else:
13                count=count+1
14                j=j-1
15        
16        return(count)
17
18        