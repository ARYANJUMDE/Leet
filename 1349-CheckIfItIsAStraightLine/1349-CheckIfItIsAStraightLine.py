# Last updated: 12/27/2025, 6:56:38 PM
class Solution(object):
    def checkStraightLine(self, coordinates):
        x_list=[]
        for i in range(1,len(coordinates)):
            x=coordinates[0][0]-coordinates[i][0]
            y=coordinates[0][1]-coordinates[i][1]
            if(x==0):
                slope=float('inf')
            else:
                slope=float(y)/float(x)

            x_list.append(slope)

        if(len(set(x_list))==1):
            return(True)
        else:
            return(False)

        
        