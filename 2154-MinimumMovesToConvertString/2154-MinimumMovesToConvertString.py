# Last updated: 7/30/2026, 11:01:46 PM
class Solution(object):
    def minimumMoves(self, s):
        count=0
        if "X" in s:
            while "X" in s:
                for i in range(0,len(s)):
                    if s[i]=="X":
                        s=s[:i]+"000"+s[i+3:]
                        count=count+1
                        break
            return(count)
        else:
            return(0)

        