# Last updated: 10/3/2026, 6:26:39 PM
1class Solution(object):
2    def maximumUnits(self, boxTypes, truckSize):
3        boxTypes.sort(key=lambda x:x[1],reverse=True)
4        count=0
5        max_size=0
6        for i in range(len(boxTypes)):
7            count=count+boxTypes[i][0]
8            if count<=truckSize:
9                max_size=max_size+boxTypes[i][0]*boxTypes[i][1]
10            else:
11                count=count-boxTypes[i][0]
12                diff=truckSize-count
13                max_size=max_size+diff*boxTypes[i][1]
14                break
15        return(max_size)
16        
17
18#         boxTypes.sort(reverse=True,key=lambda boxTypes:boxTypes[1])
19#         self.total_unit=0
20#         for self.boxcount,self.unitperbox in boxTypes:
21#             if(truckSize>=self.boxcount):
22#                 self.total_unit=self.total_unit+self.boxcount*self.unitperbox
23#                 truckSize=truckSize-self.boxcount
24#             else:
25#                 self.total_unit=self.total_unit+truckSize*self.unitperbox
26#                 break
27#         return self.total_unit
28# s=Solution()
29# s.maximumUnits([[1,3],[2,2],[3,1]],4)
30