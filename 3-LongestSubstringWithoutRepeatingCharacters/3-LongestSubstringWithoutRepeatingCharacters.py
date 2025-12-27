# Last updated: 12/27/2025, 6:58:33 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0
        for i in range(n):
            seen = set()
            curr_len = 0
            for j in range(i, n):
                if s[j] in seen:   
                    break
                seen.add(s[j])
                curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len


S=Solution()
S.lengthOfLongestSubstring("abcabcbb")      
        