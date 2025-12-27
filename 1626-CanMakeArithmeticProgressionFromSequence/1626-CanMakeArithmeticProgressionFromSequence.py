# Last updated: 12/27/2025, 6:56:30 PM
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if(len(arr)<=2):
            return True
        for i in range(len(arr)-2):
            x=arr[i+1]-arr[i]
            y=arr[i+2]-arr[i+1]
            t=True
            if(x!=y):
                t=False
                break
        if(t==True):
            return True
        else:
            return False

        