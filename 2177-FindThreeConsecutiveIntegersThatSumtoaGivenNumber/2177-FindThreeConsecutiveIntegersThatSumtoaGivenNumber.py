# Last updated: 11/10/2026, 2:29:50 PM
1class Solution:
2    def sumOfThree(self, num: int) -> list[int]:
3        if num%3==0:
4            i=(num//3)
5            return [i-1,i,i+1]
6        return []