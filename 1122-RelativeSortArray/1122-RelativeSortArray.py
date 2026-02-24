# Last updated: 2/24/2026, 3:16:40 PM
1class Solution(object):
2    def relativeSortArray(self, arr1, arr2):
3        x=[]
4        y=[]
5        for i in range(len(arr2)):
6            for j in range(len(arr1)):
7                if arr2[i]==arr1[j]:
8                    x.append(arr2[i])
9        arr1.sort()
10        for num in arr1:
11            if num not in x:
12                y.append(num)          
13        
14        return(x+y)
15