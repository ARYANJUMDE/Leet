# Last updated: 2/23/2026, 1:24:46 PM
1class Solution(object):
2    def mostWordsFound(self, sentences):
3        x=[]
4        for i in range(len(sentences)):
5            x.append(len(sentences[i].split()))
6        return(max(x))
7        