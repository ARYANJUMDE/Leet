# Last updated: 12/27/2025, 6:57:06 PM
class Solution(object):
    def checkSubarraySum(self, nums, k):
        # l=[]
        # x=[]
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         if(len(nums[i:j])>=2):
        #             l.append(nums[i:j])
        # for t in range(0,len(l)):
        #     x.append(sum(l[t]))
        # for num in x:
        #     if(num%k==0):

        #         return(True)
        #         break
        # else:
            
        #     return(False)
        mod_map = {0: -1}   # remainder → first index
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            if mod in mod_map:
                if i - mod_map[mod] >= 2:
                    return True
            else:
                mod_map[mod] = i
        return False

        