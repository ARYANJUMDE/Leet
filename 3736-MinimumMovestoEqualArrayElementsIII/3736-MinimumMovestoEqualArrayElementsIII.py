# Last updated: 11/3/2026, 6:14:27 PM
1class Solution(object):
2    def minMoves(self, nums):
3        moves=0
4        nums.sort()
5        maxi=nums[-1]
6        for i in range(len(nums)-1):
7            moves=moves+maxi-nums[i]
8        return moves
9        