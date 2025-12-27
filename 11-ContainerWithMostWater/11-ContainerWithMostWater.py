# Last updated: 12/27/2025, 6:58:27 PM
class Solution(object):
    def maxArea(self, height):
        # max=0
        # for i in range(0,len(height)):
        #     for j in range(0,len(height)):
        #         area=min(height[i],height[j])*(j-i)
        #         if area>max:
        #             max=area
        # return max
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

