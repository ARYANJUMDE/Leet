# Last updated: 12/27/2025, 6:57:43 PM
class Solution(object):
    def addDigits(self, num):
        # while(num>=10):
        #     s=0
        #     while(num>0):
        #         s=s+num%10
        #         num=num//10
        #     num=s
        # return num
        if(num==0):
            return 0
        else:
            return 1+(num-1)%9

        