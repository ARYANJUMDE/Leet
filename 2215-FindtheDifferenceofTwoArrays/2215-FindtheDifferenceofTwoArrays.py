# Last updated: 4/8/2026, 9:28:26 AM
1class Solution(object):
2    def findDifference(self, nums1, nums2):
3        result1=[]
4        result2=[]
5        x=[]
6        for num in nums1:
7            if num not in nums2:
8                if num not in result1:
9                    result1.append(num)
10        for num in nums2:
11            if num not in nums1:
12                if num not in result2:
13
14                    result2.append(num)
15        x.append(result1)
16        x.append(result2)
17        
18        return(x)