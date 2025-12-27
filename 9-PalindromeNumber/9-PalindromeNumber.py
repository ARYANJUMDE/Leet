# Last updated: 12/27/2025, 6:58:29 PM
class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if(x==x[::-1]):
            return True
        else:
            return False
s=Solution()
s.isPalindrome(121)


        