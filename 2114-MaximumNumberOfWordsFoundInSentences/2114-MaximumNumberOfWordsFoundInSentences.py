# Last updated: 9/9/2026, 10:11:12 PM
class Solution(object):
    def mostWordsFound(self, sentences):
        x=[]
        for i in range(len(sentences)):
            x.append(len(sentences[i].split()))
        return(max(x))
        