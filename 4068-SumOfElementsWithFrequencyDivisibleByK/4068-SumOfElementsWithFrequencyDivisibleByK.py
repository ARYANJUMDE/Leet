# Last updated: 12/27/2025, 6:56:07 PM
class Solution(object):
    def sumDivisibleByK(self, nums, k):
        sum1=0
        for num in nums:
            if(nums.count(num)%k==0):
                sum1=sum1+num
        return(sum1)

        