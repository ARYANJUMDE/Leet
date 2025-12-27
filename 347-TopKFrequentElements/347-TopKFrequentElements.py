# Last updated: 12/27/2025, 6:57:32 PM
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        # dicti={}
        # l=[]
        # for n in nums:
        #     dicti[n]=nums.count(n)
        # x=sorted(dicti.items(),key=lambda x: x[1],reverse=True)
        # for i in range(k):
        #     l.append(x[i][0])
        
        freq = Counter(nums)
        
        l = [num for num, count in freq.most_common(k)]
        return(l)
        
        #return(l)
        