# Last updated: 9/9/2026, 10:12:48 PM
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        word1=''.join(word1)
        word2=''.join(word2)
        if(word1==word2):
            return(True)
        else:
            return(False)
        