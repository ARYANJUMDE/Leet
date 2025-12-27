# Last updated: 12/27/2025, 6:56:33 PM
class Solution(object):
    def checkIfExist(self, arr):
        x=[]
        # for num in arr:
        #     for i in range(0,len(arr)):
        #         if(num==2*arr[i]):
        #             x.append(num)
        for num in arr:
            if(arr.count(0)>1):
                x.append(num)
            if (num!=0):
                if(2*num in arr):
                    x.append(num)
        if(len(x)!=0):
            
            return(True)
        else:
            return(False)

        