# Last updated: 9/29/2026, 6:49:21 PM
1class Solution(object):
2    def isTrionic(self, nums):
3        # count1=0
4        # count2=0
5        # if nums[0]<nums[1]:
6        #     for i in range(0,len(nums)-1):
7        #         if nums[i]<nums[i+1]:
8        #             count1=count1+1
9        #         else:
10        #             break
11        #     for i in range(i,len(nums)-1):
12        #         if nums[i]>nums[i+1]:
13        #             count2=count2+1
14        #         else:
15        #             break
16        #     for i in range(i,len(nums)-1):
17        #         if nums[i]<nums[i+1]:
18        #             count1=count1+1
19        #         else:
20        #             break
21        # if count1+count2+1==len(nums):
22        #     return True
23        # return False
24        count1=0
25        count2=0
26        count3=0
27        for i in range(0,len(nums)-1):
28            if nums[i]<nums[i+1]:
29                count1=count1+1
30            else:
31                break
32        if count1>0:
33            for i in range(i,len(nums)-1):
34                if nums[i]>nums[i+1]:
35                    count2=count2+1
36                else:
37                    break
38        else:
39            return False
40        if count1>0 and count2>0:
41            for i in range(i,len(nums)-1):
42                if nums[i]<nums[i+1]:
43                    count3=count3+1
44                else:
45                    break
46        else:
47            return False
48        if count1>0 and count2>0 and count3>0:
49            if count1+count2+count3+1==len(nums):
50                return True
51        return False
52
53
54