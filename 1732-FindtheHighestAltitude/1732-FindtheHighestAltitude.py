# Last updated: 2/23/2026, 1:14:07 PM
1class Solution(object):
2    def largestAltitude(self, gain):
3        altitude=0
4        x=[0]
5        for i in range(len(gain)):
6            altitude=altitude+gain[i]
7            x.append(altitude)
8        
9        return(max(x))
10        