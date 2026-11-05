# Last updated: 11/5/2026, 10:12:35 AM
1class Solution(object):
2    def findTheDistanceValue(self, arr1, arr2, d):
3        count=0
4        for i in range(0,len(arr1)):
5            y=True
6            for j in range(0,len(arr2)):
7                x=abs(arr1[i]-arr2[j])
8                if(x<=d):
9                    y=False
10                    break
11            if(y==True):
12                count=count+1
13            
14        return(count)
15        