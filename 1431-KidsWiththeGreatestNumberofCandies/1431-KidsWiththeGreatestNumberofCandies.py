# Last updated: 4/2/2026, 12:05:36 PM
1class Solution(object):
2    def kidsWithCandies(self, candies, extraCandies):
3        result=[]
4        for i in range(len(candies)):
5            if(candies[i]+extraCandies>=max(candies)):
6                result.append(True)
7            else:
8                result.append(False)
9        return(result)
10        