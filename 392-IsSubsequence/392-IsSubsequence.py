# Last updated: 12/27/2025, 6:57:20 PM
class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        while i<len(s) and j<len(t):
            if(s[i]==t[j]):
                i=i+1
            j=j+1
        if i==len(s):
            return True
        else:
            return False

        