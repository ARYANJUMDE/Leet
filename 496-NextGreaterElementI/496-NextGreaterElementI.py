# Last updated: 2/16/2026, 4:42:51 PM
1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3        x=[]
4        for num in nums1:
5            if num in nums2:
6                t=nums2.index(num)
7            for i in range(t,len(nums2)):
8                if nums2[i]>num:
9                    x.append(nums2[i])
10                    break
11            else:
12                x.append(-1)
13        
14        return(x)
15        