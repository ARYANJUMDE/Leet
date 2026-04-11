# Last updated: 4/11/2026, 12:16:07 PM
1class Solution(object):
2    def finalPrices(self, prices):
3        answer=[]
4        for i in range(len(prices)):
5            for j in range(i+1,len(prices)):
6                if prices[i]>=prices[j]:
7                    
8                    answer.append(prices[i]-prices[j])
9                    break
10            else:
11                answer.append(prices[i])
12        return(answer)