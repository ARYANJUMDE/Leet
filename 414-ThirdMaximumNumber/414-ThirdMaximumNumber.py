# Last updated: 12/27/2025, 6:57:16 PM
class Solution(object):
    def thirdMax(self, nums):
        nums.sort(reverse=True)
        ans=[]
        for num in nums:
            if(num not in ans):
                ans.append(num)
        if(len(ans)<3):
            return (max(ans))
        else:
            return (ans[2])

        