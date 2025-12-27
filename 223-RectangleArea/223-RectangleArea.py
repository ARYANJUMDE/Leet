# Last updated: 12/27/2025, 6:57:47 PM
import math
class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

        ax3=max(0,min(ax2,bx2)-max(ax1,bx1))
        ay3=max(0,min(ay2,by2)-max(ay1,by1))
        len1=math.sqrt((ax1-ax2)**2)
        bre1=math.sqrt((ay1-ay2)**2)
        len2=math.sqrt((bx1-bx2)**2)
        bre2=math.sqrt((by1-by2)**2)
        area1=len1*bre1
        area2=len2*bre2
        
        common_area=ax3*ay3
        
        
        
        total=(area1+area2-common_area)
        return int(total)


        