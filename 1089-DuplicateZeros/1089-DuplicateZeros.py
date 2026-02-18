# Last updated: 2/18/2026, 4:13:48 PM
1class Solution(object):
2    def duplicateZeros(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: None Do not return anything, modify arr in-place instead.
6        """
7        i=0
8        x=0
9        z=len(arr)
10        while i<z:
11            if(x!=z):
12                if arr[i]==0:
13                    arr.insert(i+1,0)
14                    arr.pop()
15                    x=x+2
16                    i=i+2
17                else:
18                    x=x+1
19                    i=i+1
20