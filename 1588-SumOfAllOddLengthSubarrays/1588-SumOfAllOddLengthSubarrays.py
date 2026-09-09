# Last updated: 9/9/2026, 10:12:59 PM
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        l=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if(len(arr[i:j])%2!=0):
                    l.append(sum(arr[i:j]))
        return(sum(l))
        