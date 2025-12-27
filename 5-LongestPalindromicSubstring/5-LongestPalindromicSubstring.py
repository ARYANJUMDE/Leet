# Last updated: 12/27/2025, 6:58:31 PM
class Solution(object):
    def longestPalindrome(self, s):
        #x=[]
        t=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                x=s[i:j]
                if(x==x[::-1]):
                    t.append(x)
                # x.append(s[i:j])
        # for k in range(0,len(x)):
        #     if(x[k]==x[k][::-1]):
        #         t.append(x[k])
        return(max(t,key=len))

        