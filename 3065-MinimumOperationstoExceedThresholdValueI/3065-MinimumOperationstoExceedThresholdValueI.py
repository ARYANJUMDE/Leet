# Last updated: 1/29/2026, 11:53:09 AM
1class Solution(object):
2    def minOperations(self, nums, k):
3        count=0
4        for num in nums:
5            if num<k:
6                count=count+1
7        
8        
9        return(count)
10        