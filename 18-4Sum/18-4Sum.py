# Last updated: 1/20/2026, 3:14:29 PM
1class Solution(object):
2    def fourSum(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        res = []
6
7        for i in range(n - 3):
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            for j in range(i + 1, n - 2):
12                if j > i + 1 and nums[j] == nums[j - 1]:
13                    continue
14
15                left, right = j + 1, n - 1
16
17                while left < right:
18                    total = nums[i] + nums[j] + nums[left] + nums[right]
19
20                    if total == target:
21                        res.append([nums[i], nums[j], nums[left], nums[right]])
22
23                        left += 1
24                        right -= 1
25
26                        while left < right and nums[left] == nums[left - 1]:
27                            left += 1
28                        while left < right and nums[right] == nums[right + 1]:
29                            right -= 1
30
31                    elif total < target:
32                        left += 1
33                    else:
34                        right -= 1
35
36        return res
37        