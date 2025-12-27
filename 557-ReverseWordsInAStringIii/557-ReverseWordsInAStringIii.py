# Last updated: 12/27/2025, 6:57:05 PM
class Solution(object):
    def reverseWords(self, s):
        # s=s.split()
        # z=[]
        # for num in s:
        #     z.append(num[::-1])
        # s=""
        # for i in range(0,len(z)):
        #     s=s+z[i]+" "   
        # return s
        
        # x=""
        
        # for num in s:
        #     x=x+num
        #     s=""
            
        #     x=x.split()
        #     z=[]
        #     for num in x:
        #         z.append(num[::-1])
        #     for i in range(0,len(z)):
        #         s=s+z[i]+" "   
        #     return s
        return " ".join(word[::-1] for word in s.split())
