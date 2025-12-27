# Last updated: 12/27/2025, 6:57:12 PM
class Solution(object):
    def findDuplicates(self, nums):
        # x=[]
        # t=[]
        # for num in nums:
        #     if num not in x:
        #         x.append(num)
        # for num in x:
        #     if(nums.count(num)==2):
        #         t.append(num)
        
        # return(t)


        t=[]
        counts={}
        
        for num in nums:
            if(num in counts):
                counts[num]=counts[num]+1
            else:
                counts[num]=1
        for num in counts:
            if(counts[num]==2):
                t.append(num)
        return t


        