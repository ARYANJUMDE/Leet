# Last updated: 5/4/2026, 10:45:22 AM
1class Solution(object):
2    def threeConsecutiveOdds(self, arr):
3        for i in range(len(arr)-2):
4            if(arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
5                return(True)
6        else:
7            return(False)
8        
9
10        