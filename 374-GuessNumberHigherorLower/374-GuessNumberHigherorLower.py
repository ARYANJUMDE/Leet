# Last updated: 1/28/2026, 4:33:29 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num):
7
8class Solution(object):
9    def guessNumber(self, n):
10        high=n
11        low=1
12        while low<=high:
13            mid=(high+low)//2
14            res=guess(mid)
15            
16            if res==0:
17                return(mid)
18            elif(res==1):
19                low=mid+1
20            else:
21                high=mid-1
22
23        