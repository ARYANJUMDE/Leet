# Last updated: 12/27/2025, 6:57:48 PM
class Solution(object):
    def isAnagram(self, s, t):
        if(sorted(s)==sorted(t)):
            return True
        else:
            return False
s=Solution()
s.isAnagram("anagram","nagaram")
        