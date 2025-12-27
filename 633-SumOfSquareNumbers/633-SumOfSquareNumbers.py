# Last updated: 12/27/2025, 6:57:01 PM
class Solution(object):
    def judgeSquareSum(self, c):
        i, j = 0, int(c**0.5)
        while i <= j:
            s = i*i + j*j
            if s == c:
                return True
            elif s < c:
                i += 1
            else:
                j -= 1
        return False


        