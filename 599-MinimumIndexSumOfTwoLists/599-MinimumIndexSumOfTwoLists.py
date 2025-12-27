# Last updated: 12/27/2025, 6:57:02 PM
class Solution(object):
    def findRestaurant(self, list1, list2):
        x=[]
        z=[]
        for i in range (len(list1)):
            for j in range(len(list2)):
                if(list1[i]==list2[j]):
                    x.append((list1[i],i+j))          
        x.sort(key=lambda t:t[1])
        y=x[0][1]
        for i in range(0,len(x)):
            if(x[i][1]==y):
                
                z.append(x[i][0])
        return(z)

        