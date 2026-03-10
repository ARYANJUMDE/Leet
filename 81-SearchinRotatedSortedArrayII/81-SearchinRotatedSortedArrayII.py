# Last updated: 3/10/2026, 4:17:21 PM
1class Solution(object):
2    def search(self, nums, target):
3        nums=list(set(nums))
4        nums.sort()
5        min1=0
6        max1=len(nums)-1
7        while min1<=max1:
8            mid=(min1+max1)//2
9            if nums[mid]==target:
10                return(True)
11            elif (nums[mid]<target):
12                min1=mid+1
13            else:
14                max1=mid-1
15        return False
16
17        