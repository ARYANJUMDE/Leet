# Last updated: 4/15/2026, 2:01:30 PM
1class Solution(object):
2    def finalValueAfterOperations(self, operations):
3        X=0
4        for i in range(len(operations)):
5            if operations[i]=='X++' or operations[i]=='++X':
6                X=X+1
7            else:
8                X=X-1
9        return(X)
10        