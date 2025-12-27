# Last updated: 12/27/2025, 6:57:26 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        x=[]
        y=[]
        count=0
        for st in ransomNote:
            x.append(st)
        #ransomeNote.split()
        #print(x)
        for st2 in magazine:
            y.append(st2)
        #print(y)
        
        for w in x:
            if(w in y):
                count=count+1
                
                y.remove(w)
        if(count==len(x)):
            return(True)
        else:
            return(False)
