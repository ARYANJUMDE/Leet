# Last updated: 10/17/2026, 6:49:58 PM
1class Solution:
2    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
3        x=[]
4        count2=0
5        for i in range(len(words)):
6            count1=0
7            for j in range(len(words[i])):
8                if words[i][j] in allowed:
9                    count1=count1+1
10                else:
11                    break
12            if count1==len(words[i]):
13                count2=count2+1
14
15        return count2
16                
17
18
19        