# Last updated: 8/19/2026, 4:24:47 PM
class Solution(object):
    def removeDuplicates(self, nums):
        t=list(set(nums))
        for i in range(len(t)):
            if nums.count(t[i])>2:
                for j in range(nums.count(t[i])-2):
                    nums.remove(t[i])
        return(len(nums))