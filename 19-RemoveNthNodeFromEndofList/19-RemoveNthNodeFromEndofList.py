# Last updated: 3/16/2026, 6:29:04 PM
1class Solution(object):
2    def isValid(self, s):
3        stack=[]
4        for ch in s:
5            if(ch in "({["):
6                stack.append(ch)
7            else:
8                if len(stack)==0:
9                    return False
10                top=stack.pop()
11
12                if ((ch==")" and top!="(") or (ch=="]" and top!="[") or (ch=="}" and top!="{")):
13
14
15                    return False
16        return len(stack)==0
17
18        
19        