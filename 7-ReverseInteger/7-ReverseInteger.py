# Last updated: 12/27/2025, 6:58:30 PM
class Solution(object):
    def reverse(self, x):
        x=str(x)
        l=list(x)
        while len(l) > 1 and l[-1] == '0':
            l.pop()
        x=''.join(l)

        if x[0]=="-":
            x="-"+x[:0:-1]
        else:
            x=x[::-1]
        x=int(x)
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x
    
S=Solution()
S.reverse(123)


        