# Last updated: 12/27/2025, 6:57:25 PM
class Solution(object):
    def superPow(self, a, b):
        # x=int("".join(str(i) for i in b))
        # t=a**x
        # if(t<1337):
        #     return t
        # else:
        #     return t%1337
        result = 1
        for d in b:
            result = (pow(result, 10, 1337) * pow(a, d, 1337)) % 1337
        return result
        