# Last updated: 12/27/2025, 6:57:29 PM
class Solution(object):
    def intersect(self, nums1, nums2):
        nums3=[]
        for num in nums1:
            if num in nums2:
                nums3.append(num)
                nums2.remove(num) ###one num is removed
        return (nums3)
        