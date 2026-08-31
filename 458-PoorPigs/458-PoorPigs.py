# Last updated: 8/31/2026, 11:15:01 PM
1import math
2
3class Solution(object):
4    def poorPigs(self, buckets, minutesToDie, minutesToTest):
5        states = (minutesToTest // minutesToDie) + 1
6        return int(math.ceil(math.log(buckets) / math.log(states) - 1e-10))