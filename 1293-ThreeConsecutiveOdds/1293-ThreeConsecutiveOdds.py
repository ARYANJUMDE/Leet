# Last updated: 5/18/2026, 12:45:24 PM
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)-2):
            if(arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
                return(True)
        else:
            return(False)
        

        