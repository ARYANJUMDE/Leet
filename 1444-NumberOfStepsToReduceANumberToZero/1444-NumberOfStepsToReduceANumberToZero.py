# Last updated: 2/28/2026, 11:54:45 AM
class Solution(object):
    def numberOfSteps(self, num):
        count=0
        while num!=0:
            if(num%2==0):
                num=num/2
            else:
                num=num-1
            count=count+1
        
        
        return(count)  
    
        