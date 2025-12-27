# Last updated: 12/27/2025, 6:58:11 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.split()
        return (len(l[-1]))
        