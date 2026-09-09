# Last updated: 9/9/2026, 10:15:06 PM
class Solution(object):
    def defangIPaddr(self, address):
        x=''
        for ch in address:
            if ch=='.':
                x=x+'[.]'
            else:
                x=x+ch
        return(x)
        