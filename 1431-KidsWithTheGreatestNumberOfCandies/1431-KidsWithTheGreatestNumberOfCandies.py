# Last updated: 9/9/2026, 10:13:31 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=max(candies)):
                result.append(True)
            else:
                result.append(False)
        return(result)
        