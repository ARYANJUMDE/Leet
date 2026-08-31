# Last updated: 8/31/2026, 9:42:00 PM
1class Solution(object):
2    def minimumDeletions(self, nums):
3        x=nums.index(max(nums))
4        y=nums.index(min(nums))
5        z=len(nums)//2
6        if x>z and y<z:
7            t=len(nums[:x+1])
8            p=len(nums[y:])
9            o=len(nums[:y+1])
10            u=len(nums[x:])
11            return min(t,p,o+u)
12        if x<z and y>z:
13            t=len(nums[:y+1])
14            p=len(nums[x:])
15            o=len(nums[:x+1])
16            u=len(nums[y:])
17            return min(t,p,o+u)
18        if x!=z and y!=z and x<z and y<z:
19            return(len(nums[:max(x,y)+1]))
20        if x!=z and y!=z and x>z and y>z:
21            return(len(nums[min(x,y):]))
22        if x==z and y<z:
23            return(z+1)
24        if y==z and x<z:
25            return z+1
26        if x==z and y>z:
27            return min(z+1,len(nums[x:y+1]))
28        if y==z and x>z:
29            return min(z+1,len(nums[y:x+1]))
30        if x==z and y==z:
31            return z+1