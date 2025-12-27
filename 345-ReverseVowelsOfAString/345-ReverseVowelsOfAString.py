# Last updated: 12/27/2025, 6:57:31 PM
class Solution(object):
    def reverseVowels(self, s):
        x=[]
        vowels=["A","E","I","O","U","a","e","i","o","u"]
        for ch in s:
            if(ch in vowels):
                x.append(ch)
                s=s.replace(ch,"_")
        x=x[::-1]
        i=0
        while(i<len(x)):
            for ch in s:
                if(ch=="_"):
                    s=s.replace("_",x[i],1)
                    i=i+1    
        return s


s=Solution()
s.reverseVowels("IceCreAm")

        