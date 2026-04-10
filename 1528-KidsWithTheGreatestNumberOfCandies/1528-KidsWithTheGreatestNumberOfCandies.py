# Last updated: 4/10/2026, 4:10:31 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=max(candies)):
                result.append(True)
            else:
                result.append(False)
        return(result)
        