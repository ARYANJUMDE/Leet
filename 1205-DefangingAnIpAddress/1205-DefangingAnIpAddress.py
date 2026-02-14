# Last updated: 2/14/2026, 11:06:16 AM
class Solution(object):
    def defangIPaddr(self, address):
        x=''
        for ch in address:
            if ch=='.':
                x=x+'[.]'
            else:
                x=x+ch
        return(x)
        