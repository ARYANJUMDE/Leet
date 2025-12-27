# Last updated: 12/27/2025, 6:58:24 PM
class Solution(object):
    def threeSum(self, nums):
        # nums.sort()
        # x=[]
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if(nums[i]+nums[j]+nums[k]==0):
        #                 triplet=[nums[i],nums[j],nums[k]]
        #                 if triplet not in x:
        #                     x.append(triplet)
        # return(x)





        nums.sort()
        x=[]
        for i in range(0,len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if(third in seen):
                    triplet=[nums[i],nums[j],third]
                    triplet.sort()
                    if triplet not in x:
                        x.append(triplet)
                seen.add(nums[j])
        return(x)

        