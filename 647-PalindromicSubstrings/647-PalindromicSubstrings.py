# Last updated: 7/13/2026, 10:09:57 PM
class Solution(object):
    def countSubstrings(self, s):
        x=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    x.append(s[i:j])
        return(len(x))
        