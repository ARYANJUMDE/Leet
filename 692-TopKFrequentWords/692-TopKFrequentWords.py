# Last updated: 12/27/2025, 6:56:57 PM
class Solution(object):
    def topKFrequent(self, words, k):
        dict1={}
        l=[]
        for num in words:
            dict1[num]=words.count(num)
        dict1=sorted(dict1.items(),key=lambda x:(-x[1],x[0]))
        for i in range(k):
            l.append(dict1[i][0])
        return (l)
S=Solution()
S.topKFrequent(["i","love","leetcode","i","love","coding"],2)

        