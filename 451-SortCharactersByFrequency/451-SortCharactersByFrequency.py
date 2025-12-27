# Last updated: 12/27/2025, 6:57:10 PM
class Solution(object):
    def frequencySort(self, s):
        from collections import Counter
        freq=Counter(s)
        p=sorted(s,key=lambda x:(freq[x],x),reverse=True)
        return(''.join(p))
        