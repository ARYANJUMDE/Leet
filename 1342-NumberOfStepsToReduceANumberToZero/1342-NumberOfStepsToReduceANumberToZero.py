# Last updated: 9/9/2026, 10:14:18 PM
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
    
        