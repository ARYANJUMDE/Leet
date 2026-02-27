# Last updated: 2/27/2026, 11:40:21 AM
class Solution(object):
    def largestAltitude(self, gain):
        altitude=0
        x=[0]
        for i in range(len(gain)):
            altitude=altitude+gain[i]
            x.append(altitude)
        
        return(max(x))
        