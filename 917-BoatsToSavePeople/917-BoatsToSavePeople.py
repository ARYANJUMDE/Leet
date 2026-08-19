# Last updated: 8/19/2026, 4:19:12 PM
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i=0
        j=len(people)-1
        count=0
        while i<=j:
            if people[i]+people[j]<=limit:
                count=count+1
                i=i+1
                j=j-1
            else:
                count=count+1
                j=j-1
        
        return(count)

        