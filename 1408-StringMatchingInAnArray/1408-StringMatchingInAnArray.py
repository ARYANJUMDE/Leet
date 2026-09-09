# Last updated: 9/9/2026, 10:13:32 PM
class Solution(object):
    def stringMatching(self, words):
        x=[]
        for i in range (len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j and words[i] not in x:
                    x.append(words[i])
        
        return(x)
        