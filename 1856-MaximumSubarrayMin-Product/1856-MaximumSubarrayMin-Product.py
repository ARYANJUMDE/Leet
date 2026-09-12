# Last updated: 9/12/2026, 4:51:39 PM
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        curr_len=0
4        final_len=0
5        l=0
6        r=0
7        t=[]
8        while r<len(s):
9            if s[r] in t:
10                while s[r] in t:
11                    t.pop(0)
12                    l=l+1
13                    curr_len=curr_len-1
14            t.append(s[r])
15            curr_len=curr_len+1
16            if curr_len>final_len:
17                final_len=curr_len
18            r=r+1
19        return(final_len)
20#         n = len(s)
21#         max_len = 0
22#         for i in range(n):
23#             seen = set()
24#             curr_len = 0
25#             for j in range(i, n):
26#                 if s[j] in seen:   
27#                     break
28#                 seen.add(s[j])
29#                 curr_len += 1
30#                 max_len = max(max_len, curr_len)
31#         return max_len
32
33
34
35# S=Solution()
36# S.lengthOfLongestSubstring("abcabcbb")      
37        