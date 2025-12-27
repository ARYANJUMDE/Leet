# Last updated: 12/27/2025, 6:56:23 PM
class Solution(object):
    def countGoodSubstrings(self, s):
        l=list(s)
        l2=[]
        for i in range(0,len(l)):
            for j in range(i+1,len(l)+1):
                l2.append(''.join(l[i:j]))
        l3=[]
        for i in range(0,len(l2)):
            if(len(l2[i])==3):
                l3.append(l2[i])
        l4=[]
        for ch in l3:
            if(len(ch)==len(set(ch))):
                l4.append(ch)
                
                
        return len(l4)


S=Solution()
S.countGoodSubstrings("xyzzaz")  

        