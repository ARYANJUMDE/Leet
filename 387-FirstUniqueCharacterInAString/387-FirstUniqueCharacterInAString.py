# Last updated: 12/27/2025, 6:57:23 PM
class Solution(object):
    def firstUniqChar(self, s):
        # for i in range(0,len(s)):
        #     if(s.count(s[i])<2):
        #         return (i)
        #         break
        # else:
        #     return -1
        l=[]
        for ch in s:
            if(ch not in l):
                l.append(ch)
        
        x=[]
        for i in range(0,len(l)):
            x.append(list((l[i],s.count(l[i]),s.index(l[i]))))
        
        y=[]
        for i in range(len(x)):
            if(x[i][1]==1):
                return(x[i][2])
                break
        else:
            return(-1)


        