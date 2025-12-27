# Last updated: 12/27/2025, 6:57:22 PM
class Solution(object):
    def findTheDifference(self, s, t):
        x = set(t)  # all unique letters in t
        for c in x:
            if t.count(c) != s.count(c):
                return (c)
                break
