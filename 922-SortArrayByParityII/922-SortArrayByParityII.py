# Last updated: 2/4/2026, 10:07:12 AM
1class Solution(object):
2    def sortArrayByParityII(self, nums):
3        # r=len(nums)//2
4        # for i in range(r):
5        #     if(i%2!=0 or nums[i]%2!=0):
6        #         for j in range(r,2*r):
7        #             nums[i],nums[j]=nums[j],nums[i]
8        #             break
9        # return(nums)
10        odd=[]
11        even=[]
12        r=len(nums)
13        for num in nums:
14            if num%2==0:
15                even.append(num)
16            else:
17                odd.append(num)
18        for i in range(r):
19            if i%2==0:
20                nums.pop(i)
21                nums.insert(i,even[0])
22                even.pop(0)
23            else:
24                nums.pop(i)
25                nums.insert(i,odd[0])
26                odd.pop(0)
27        return nums
28
29
30        