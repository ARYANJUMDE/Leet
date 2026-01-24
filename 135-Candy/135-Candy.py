# Last updated: 1/24/2026, 9:10:05 PM
1class Solution(object):
2    def candy(self, ratings):
3        candies=[1]*len(ratings)
4        for i in range(0,len(ratings)-1):
5            if ratings[i]<ratings[i+1]:
6                candies[i+1]=candies[i]+1
7        for i in range(len(ratings)-1,0,-1):
8            if ratings[i-1]>ratings[i] and candies[i-1]<=candies[i]:
9                candies[i-1]=candies[i]+1
10        return(sum(candies))
11
12        