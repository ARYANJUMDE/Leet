# Last updated: 10/31/2026, 10:03:47 AM
1class Solution(object):
2    def twoOutOfThree(self, nums1, nums2, nums3):
3        x=[]
4        for i in range(len(nums1)):
5            if nums1[i] in nums2:
6                x.append(nums1[i])
7            elif nums1[i] in nums3:
8                x.append(nums1[i])
9        for i in range(len(nums2)):
10            if nums2[i] in nums1:
11                x.append(nums2[i])
12            elif nums2[i] in nums3:
13                x.append(nums2[i])
14        for i in range(len(nums3)):
15            if nums3[i] in nums1:
16                x.append(nums3[i])
17            elif nums3[i] in nums2:
18                x.append(nums3[i])
19        return list(set(x))
20        
21        