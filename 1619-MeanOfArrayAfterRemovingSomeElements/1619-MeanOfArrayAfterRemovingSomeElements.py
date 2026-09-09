# Last updated: 9/9/2026, 10:15:04 PM
class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        k=int(len(arr)*0.05)
        x=float(sum(arr[k:-k]))/len(arr[k:-k])
        return x
        