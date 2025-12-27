# Last updated: 12/27/2025, 6:57:46 PM
class Solution(object):
    def majorityElement(self, nums):
        x=len(nums)//3
        a=[]
        freq={}
        # for num in nums:
        #     if(nums.count(num)>x and num not in a):
        #         a.append(num)
        # return(a)
        for num in nums:
            if(num in freq):
                freq[num]=freq[num]+1
            else:
                freq[num]=1
        for num in freq:
            if(freq[num]>x):
                a.append(num)
        return a
        