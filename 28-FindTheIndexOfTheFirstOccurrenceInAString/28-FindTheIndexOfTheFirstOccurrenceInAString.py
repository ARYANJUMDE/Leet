# Last updated: 12/27/2025, 6:58:18 PM
class Solution(object):
    def strStr(self, haystack, needle):
        index=haystack.find(needle)
        if(index!=-1):
            return index
        else:
            return -1
s=Solution()
s.strStr("sadbutsad","sad")
        