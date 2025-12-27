# Last updated: 12/27/2025, 6:58:23 PM
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         from itertools import combinations
#         r=3
#         x=[]
#         result=combinations(nums,r)
#         for comb in result:
#             x.append(sum(comb))
#         mini=abs(target-x[0])
#         cls_sum=x[0]
#         for i in range(1,len(x)):
#             diff=abs(target-x[i])
#             if(diff<mini):
#                 mini=diff
#                 cls_sum=x[i]
                
#         return (cls_sum)
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  # initialize with first 3

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # update closest sum if this is better
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    l += 1   # need a bigger sum
                elif curr_sum > target:
                    r -= 1   # need a smaller sum
                else:
                    return target  # exact match, best possible

        return closest_sum


        
        