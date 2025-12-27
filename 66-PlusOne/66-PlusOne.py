# Last updated: 12/27/2025, 6:58:10 PM
class Solution(object):
    def plusOne(self, digits):
        s=" "
        for i in range(0,len(digits)):
            s=s+str(digits[i])
        t1=list(str(int(s)+1))
        for i in range(0,len(t1)):
            t1[i]=int(t1[i])
        return t1