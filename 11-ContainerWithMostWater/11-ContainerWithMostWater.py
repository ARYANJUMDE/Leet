# Last updated: 9/20/2026, 6:51:10 PM
1class Solution(object):
2    def maxArea(self, height):
3        # max=0
4        # for i in range(0,len(height)):
5        #     for j in range(0,len(height)):
6        #         area=min(height[i],height[j])*(j-i)
7        #         if area>max:
8        #             max=area
9        # return max
10        # left, right = 0, len(height) - 1
11        # max_area = 0
12        # while left < right:
13        #     width = right - left
14        #     area = min(height[left], height[right]) * width
15        #     max_area = max(max_area, area)
16            
17        #     if height[left] < height[right]:
18        #         left += 1
19        #     else:
20        #         right -= 1
21        # return max_area
22
23        i=0
24        j=len(height)-1
25        max_area=0
26        while i<j:
27            width=j-i
28            heights=min(height[i],height[j])
29            area=width*heights
30            if area>max_area:
31                max_area=area
32            if height[j]>height[i]:
33                i=i+1
34            else:
35                j=j-1
36        return max_area
37            
38
39