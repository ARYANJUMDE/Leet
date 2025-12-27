# Last updated: 12/27/2025, 6:57:21 PM
class Solution(object):
    def findNthDigit(self, n):
        # count=0
        # p=0
        # for i in range(1,n+1):
        #     x=str(i)
        #     y=len(x)
        #     p=p+1
        #     count=count+y
        #     if(count==n):
        #         t=n-p
        #         return(int(str(x)[t]))
                
        #         break



        # count=0
        # i=1
        # while True:
        #     s=str(i)
        #     for ch in s:
        #         count=count+1
        #         if(count==n):
        #             return(int(ch))
        #             break
        #     if(count==n):
        #         break
                
        #     i=i+1
        digit_length = 1
        count = 9
        start = 1
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        number = start + (n - 1) // digit_length
        return int(str(number)[(n - 1) % digit_length])


        