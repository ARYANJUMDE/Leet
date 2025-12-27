# Last updated: 12/27/2025, 6:56:25 PM
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(reverse=True,key=lambda boxTypes:boxTypes[1])
        self.total_unit=0
        for self.boxcount,self.unitperbox in boxTypes:
            if(truckSize>=self.boxcount):
                self.total_unit=self.total_unit+self.boxcount*self.unitperbox
                truckSize=truckSize-self.boxcount
            else:
                self.total_unit=self.total_unit+truckSize*self.unitperbox
                break
        return self.total_unit
s=Solution()
s.maximumUnits([[1,3],[2,2],[3,1]],4)
