# Last updated: 9/9/2026, 10:09:42 PM
class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        count=0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]>0:
                count=count+1
                for j in range(i+1,len(batteryPercentages)):
                    if(batteryPercentages[j]>0):
                        batteryPercentages[j]=batteryPercentages[j]-1
        return(count)

        