# Last updated: 5/22/2026, 4:28:40 PM
1class Solution(object):
2    def decodeString(self, s):
3        stack=[]
4        for ch in s:
5            if ch != "]":
6                stack.append(ch)
7            else:
8                temp=""
9                while stack[-1]!='[':
10                    temp=stack.pop()+temp
11                stack.pop()
12                num=""
13                while stack and stack[-1].isdigit():
14                    num=stack.pop()+num
15                stack.append(temp*int(num))
16        return("".join(stack))
17
18        