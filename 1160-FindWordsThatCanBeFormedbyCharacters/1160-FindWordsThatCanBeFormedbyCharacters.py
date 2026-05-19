# Last updated: 5/19/2026, 2:42:30 PM
1class Solution(object):
2    def countCharacters(self, words, chars):
3        x=0
4        for i in range(len(words)):
5            if all(words[i].count(ch) <= chars.count(ch) for ch in words[i]):
6                x=x+len(words[i])
7        
8        
9        return(x)
10
11        