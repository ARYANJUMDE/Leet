# Last updated: 3/19/2026, 10:58:12 AM
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        if(len(flowerbed)==1):
4            if flowerbed[0]==0:
5                n=n-1
6            return n<=0
7        if flowerbed[0]==0 and flowerbed[1]==0:
8            flowerbed[0]=1
9            n=n-1
10        for i in range(len(flowerbed)-2):
11            if(flowerbed[i]==0 and flowerbed[i+2]==0 and flowerbed[i+1]!=1):
12                flowerbed[i+1]=1
13                n=n-1
14                if(n==0):
15                    return(True)
16        if(flowerbed[-1]==0 and flowerbed[-2]==0):
17            
18            n=n-1
19        return n<=0
20
21
22        