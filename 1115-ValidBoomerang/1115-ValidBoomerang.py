# Last updated: 12/27/2025, 6:56:43 PM
class Solution(object):
    def isBoomerang(self, points):
        # x=[]
        # for i in range(len(points)):
        #     if(points[i] not in x):
        #         x.append(points[i])
        # if(len(x)!=len(points)):
        #     return False
        # else:
        #     z=[]
        #     x1,y1=points[0]
        #     for i in range(len(points)-1):
        #         x2,y2=points[i]
        #         if x2-x1!=0:
        #             slope=((y2-y1)/(x2-x1))
        #         else:
        #             slope=float('inf')
        #         z.append(slope)
        #     if(not all(s==z[0] for s in z)):
                
        #         return True
        #     else:
        #         return False
        (x1, y1), (x2, y2), (x3, y3) = points
        if len(set(map(tuple, points))) != 3:
            return False
        
        return (x2 - x1)*(y3 - y1) != (x3 - x1)*(y2 - y1)
