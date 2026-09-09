# Last updated: 9/9/2026, 4:51:02 PM
1class Solution(object):
2    def countCommas(self, n):
3        p=str(n)
4        if len(p)<4:
5            return 0
6        else:
7            if len(p)<=6:
8                return n-1000+1
9            else:
10                t=999999-1000+1
11                count1=0
12                count2=0
13                for i in range(7,17):
14                    if len(str(n))==i:
15                        count2=count2+(n-(10**(i-1))+1)*((i-1)//3)
16                        count2=count2+count1+t
17                        return count2
18                    if len(str(n))>i:
19                        count1=count1+(9*(10)**(i-1))*((i-1)//3)
20                    
21
22                
23
24
25        