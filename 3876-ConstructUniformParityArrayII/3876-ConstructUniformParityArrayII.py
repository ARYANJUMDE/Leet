# Last updated: 9/3/2026, 4:43:50 PM
1class Solution(object):
2    def uniformArray(self, nums1):
3        count=0
4        for i in range(len(nums1)):
5            if nums1[i]%2==0:
6                count=count+1
7        if count==len(nums1):
8            return True
9        if min(nums1)%2==0:
10            return False
11        return True
12
13        # nums1.sort()
14        # count=0
15        # for i in range(len(nums1)):
16        #     if nums1[i]%2!=0:
17        #         count=count+1
18        #     if nums1[i]%2==0 and count>0:
19        #         continue
20        #     else:
21        #         return False
22        # return True
23            
24        