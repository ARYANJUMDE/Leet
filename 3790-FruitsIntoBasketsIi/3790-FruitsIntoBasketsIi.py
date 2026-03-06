# Last updated: 3/6/2026, 4:48:00 PM
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        x=[]
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if(baskets[j]>=fruits[i]):
                    x.append(fruits[i])
                    baskets.pop(j)
                    break
        
        return(len(fruits)-len(x))

        