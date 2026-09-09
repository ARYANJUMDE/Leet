# Last updated: 9/9/2026, 10:08:43 PM
class Solution(object):
    def sumDivisibleByK(self, nums, k):
        sum1=0
        for num in nums:
            if(nums.count(num)%k==0):
                sum1=sum1+num
        return(sum1)

        