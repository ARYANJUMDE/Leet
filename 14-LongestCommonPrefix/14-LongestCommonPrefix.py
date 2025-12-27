# Last updated: 12/27/2025, 6:58:25 PM
from collections import Counter
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        x=[]
        for word in strs:
            for i in range(0,len(word)):
                for j in range(i+1,len(word)+1):
                    x.append(word[i:j])
        count=Counter(x)
        if not count: 
            return ""
        max_value=max(count.values())
        answer = ""
        for sub, freq in count.items():
            if all(w.startswith(sub) for w in strs):
                if len(sub) > len(answer):
                     answer = sub
        return answer


s=Solution()
s.longestCommonPrefix(["flower","flow","flight"])
       