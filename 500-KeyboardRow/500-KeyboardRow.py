# Last updated: 12/27/2025, 6:57:09 PM
class Solution(object):
    def findWords(self, words):
        x=[]
        st1="qwertyuiop"
        st2="asdfghjkl"
        st3="zxcvbnm"

        for word in words:
            y=word.lower()
            if all(ch in st1 for ch in y):
                x.append(word)
            elif all(ch in st2 for ch in y):
                x.append(word)
            elif all(ch in st3 for ch in y):
                x.append(word)
        return(x)
