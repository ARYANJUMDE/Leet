# Last updated: 12/27/2025, 6:56:48 PM
# class Solution(object):
#     def largestPerimeter(self, nums):
#         from itertools import combinations
#         x=[]
#         t=[]
#         result=combinations(nums,3)
#         for com in result:
#             x.append(sorted(com))
#         for i in range(0,len(x)):
#             if(x[i][0]+x[i][1]>x[i][2]):
#                 t.append(x[i][0]+x[i][1]+x[i][2])
#         if(len(t)==0):
            
#             return (0)
            
#         else:
            
#             return(max(t))
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)  # sort descending
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a < b + c:   # triangle condition
                return a + b + c
        return 0
