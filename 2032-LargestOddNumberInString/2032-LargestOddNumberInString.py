# Last updated: 12/27/2025, 6:56:22 PM
# class Solution(object):
#     def largestOddNumber(self, num):
#         x=int(num)
#         if(x%2!=0):
#             return(str(x))
#         else:
#             x=[]
#             y=[]
#             for nums in num:
#                 x.append(int(nums))
#             for i in range(len(x)):
#                 if(x[i]%2!=0):
                    
#                     y.append(x[i])
#             if(len(y)==0):
#                 return("")
            
#             else:
#                 return(str(max(y)))

class Solution(object):
    def largestOddNumber(self, num):
        # Start checking from the end of the string
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ""
