# Last updated: 12/27/2025, 6:58:04 PM
class Solution(object):
    def isPalindrome(self, s):
        x=s.lower()
        y=x.replace(" ","")
        alpha=[]
        for i in range (97,123):
            alpha.append(chr(i))
        for i in range(0,10):
            alpha.append(str(i))
        for letter in y:
            if(letter not in alpha):
                y=y.replace(letter,"")
        if(y==y[::-1]):
            return True
        else:
            return False
p=Solution()

p.isPalindrome("A man, a plan, a canal:Panama")
        