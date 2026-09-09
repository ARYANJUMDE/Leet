# Last updated: 9/9/2026, 10:11:31 PM
class Solution(object):
    def kthDistinct(self, arr, k):
        x=[]
        for ch in arr:
            if arr.count(ch)==1:
                x.append(ch)
        if(len(x)<k):
            return("")
        else:
            return(x[k-1])
