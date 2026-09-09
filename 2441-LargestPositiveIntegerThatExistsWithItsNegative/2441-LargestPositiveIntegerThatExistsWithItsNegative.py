# Last updated: 9/9/2026, 10:10:22 PM
class Solution(object):
    def findMaxK(self, nums):
        nums.sort(reverse=True) 
        #print(nums)
        x=[]
        for num in nums:
            if(num and -(num) in nums):
                x.append(num)
        
        if(len(x)!=0):
            return max(x)
        else:
            return -1



    


        