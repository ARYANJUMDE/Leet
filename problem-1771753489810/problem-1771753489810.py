# Last updated: 2/22/2026, 3:14:49 PM
1class Solution(object):
2    def numberOfSteps(self, num):
3        count=0
4        while num!=0:
5            if(num%2==0):
6                num=num/2
7            else:
8                num=num-1
9            count=count+1
10        
11        
12        return(count)  
13    
14        