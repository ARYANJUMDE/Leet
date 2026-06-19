# Last updated: 6/19/2026, 10:00:55 AM
1class Solution(object):
2    def stringMatching(self, words):
3        x=[]
4        for i in range (len(words)):
5            for j in range(len(words)):
6                if words[i] in words[j] and i != j and words[i] not in x:
7                    x.append(words[i])
8        
9        return(x)
10        