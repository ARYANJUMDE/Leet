# Last updated: 3/6/2026, 4:48:33 PM
class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        k=int(len(arr)*0.05)
        x=float(sum(arr[k:-k]))/len(arr[k:-k])
        return x
        