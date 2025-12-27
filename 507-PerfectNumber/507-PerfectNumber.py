# Last updated: 12/27/2025, 6:57:08 PM
class Solution(object):
    def checkPerfectNumber(self, num):
        # a=[]
        # for i in range(1,num):
        #     if(num%i==0):
        #         a.append(i)
        # if(sum(a)==num):
        #     return True
        # else:
        #     return False
        return num > 1 and sum({i for i in range(1, int(math.sqrt(num))+1) if num % i == 0 for i in (i, num//i)}) - num == num