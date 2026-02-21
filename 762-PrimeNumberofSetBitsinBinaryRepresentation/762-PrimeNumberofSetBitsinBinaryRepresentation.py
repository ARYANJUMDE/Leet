# Last updated: 2/21/2026, 12:14:08 PM
1class Solution(object):
2    def countPrimeSetBits(self, left, right):
3        x=[]
4        y=[]
5        for i in range(left,right+1):
6            x.append(bin(i)[2:])
7        for bi in x:
8            y.append(bi.count('1'))
9        count2=0
10        for num in y: 
11            count1=0
12            for i in range(1,num+1):
13                if num%i==0:
14                    count1=count1+1
15            if(count1==2):
16                count2=count2+1
17        
18        return(count2)
19    
20
21        