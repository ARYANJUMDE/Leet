# Last updated: 7/2/2026, 8:20:21 PM
1class Solution(object):
2    def subarraySum(self, nums, k):
3        # count=0
4        # z=[]
5        # t=[]
6        # for i in range(len(nums)):
7        #     for j in range(i+1,len(nums)+1):
8        #         z.append(nums[i:j])
9        # for i in range(len(z)):
10        #     t.append(sum(z[i]))         
11        # return(t.count(k))
12        count=0
13        x=[nums[0]]
14        for i in range(1,len(nums)):
15            x.append(x[-1]+nums[i])
16
17# x=[1,3,4,6,7]
18
19# suppose we are at index 3 ie 6 and we want a subarray whose sum is 3
20# now we need to subtract some number from 6 to get 3 ie we need to subtract 3
21# from 6 to get target so have we seen 3 before 6 ie Yes so there exists a subarray
22        hashmap={0:1}
23        for i in range(len(x)):
24            if x[i]-k in hashmap:
25                count=count+hashmap[x[i]-k]
26            if x[i] in hashmap:
27                hashmap[x[i]]=hashmap[x[i]]+1
28            else:
29                hashmap[x[i]]=1
30        return(count)            