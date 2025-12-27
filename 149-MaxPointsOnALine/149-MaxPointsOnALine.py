# Last updated: 12/27/2025, 6:57:58 PM
class Solution(object):
    def maxPoints(self, points):
        if(len(points)<3):
            return len(points)
        max_count=2 ###atleast two points to form a line
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                count=2# since we take those two point on line
                x1,y1=points[i]
                x2,y2=points[j]
                for k in range(0,len(points)):
                    if(k!=i and k!=j):
                        x3,y3=points[k]### two points to line pe hai ab thrid point ko check karege
                        if(((y2-y1)*(x3-x1))==(y3-y1)*(x2-x1)):
                            count=count+1
                max_count=max(max_count,count)
        return max_count    

        
S=Solution()
S.maxPoints([[1,1],[2,2],[3,3]])        