# Last updated: 2/7/2026, 11:40:26 PM
1class Solution(object):
2    def uncommonFromSentences(self, s1, s2):
3        x=[]
4        y=s1.split()
5        z=s2.split()
6        for word in y:
7            if word not in z and y.count(word)<2:
8                x.append(word)
9        for word in z:
10            if word not in y and z.count(word)<2:
11                x.append(word) 
12        return(x)
13        