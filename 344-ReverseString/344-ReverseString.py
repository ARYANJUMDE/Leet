# Last updated: 12/27/2025, 6:57:34 PM
class Solution(object):
    def reverseString(self, s):
        #return s[::-1]
        left,right=0,len(s)-1
        while (left<right):
            s[left],s[right]=s[right],s[left]
            left=left+1
            right=right-1
        return s

    
S=Solution()
S.reverseString(["h","e","l","l","o"])
        