# Last updated: 12/27/2025, 6:56:20 PM
class Solution(object):
    def maxSubsequence(self, nums, k):
        l=[]
        temp=nums[:]
        for i in range(0,k):
            max_val=temp[0]
            for j in range(1,len(temp)):
                if(temp[j]>max_val):
                    max_val=temp[j]
            l.append(max_val)
            temp.remove(max_val)
        result=[x for x in nums if x in l and l.remove(x) is None]
        return result

        