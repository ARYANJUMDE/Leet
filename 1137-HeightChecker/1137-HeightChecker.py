# Last updated: 12/27/2025, 6:56:41 PM
class Solution(object):
    def heightChecker(self, heights):
        x=[]
        count=0
        for i in range(len(heights)):
            x.append(heights[i])
        x.sort()
        for i in range(0,len(heights)):
            if(heights[i]!=x[i]):
                count=count+1
        return (count)

        