# Last updated: 2/28/2026, 11:54:24 AM
class Solution(object):
    def percentageLetter(self, s, letter):
        count=0
        for ch in s:
            if ch==letter:
                count=count+1
        t=((count*100//len(s)))
        return t
        