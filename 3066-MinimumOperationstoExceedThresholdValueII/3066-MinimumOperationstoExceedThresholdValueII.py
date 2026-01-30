# Last updated: 1/30/2026, 3:47:30 PM
1class Solution(object):
2    def minOperations(self, nums, k):
3        count=0
4        # while all(num>=k for num in nums)==False:
5        #     min_num1=min(nums)
6        #     nums.remove(min_num1)
7        #     min_num2=min(nums)
8        #     nums.remove(min_num2)
9
10        #     nums.append(min(min_num1,min_num2)*2+max(min_num1,min_num2))
11        #     count=count+1
12        # return(count)
13        
14        # nums.sort()
15        # i=0
16        # while i<len(nums) and nums[i]<k:
17        #     min1=nums[i]
18        #     min2=nums[i+1]
19        #     i=i+2
20        #     new_val=min1*2+min2
21        #     nums.append(new_val)
22        #     nums.sort()
23        #     count=count+1
24        # return count
25        heapq.heapify(nums)
26        while nums[0]<k:
27            min1=heapq.heappop(nums)
28            min2=heapq.heappop(nums)
29            new=min1*2+min2
30            heapq.heappush(nums,new)
31            count=count+1
32        return(count)
33