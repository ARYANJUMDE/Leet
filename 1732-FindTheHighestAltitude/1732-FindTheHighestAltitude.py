# Last updated: 9/9/2026, 10:12:32 PM
class Solution(object):
    def largestAltitude(self, gain):
        altitude=0
        x=[0]
        for i in range(len(gain)):
            altitude=altitude+gain[i]
            x.append(altitude)
        
        return(max(x))
        