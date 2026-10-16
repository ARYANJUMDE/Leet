# Last updated: 10/16/2026, 8:35:38 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        x=[]
4        for ch in s:
5            if ch=='(' or ch=='[' or ch=='{':
6                x.append(ch)
7            else:
8                if len(x)==0:
9                    return False
10                t=x.pop()
11                if ch==")" and t=="(":
12                    continue
13                elif ch=="]" and t=="[":
14                    continue
15                elif ch=="}" and t=="{":
16                    continue
17                else:
18                    return False
19        if len(x)==0:
20            return True
21        else:
22            return False
23                    
24