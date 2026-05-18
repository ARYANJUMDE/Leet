# Last updated: 5/18/2026, 12:33:23 PM
1class Solution(object):
2    def maxSum(self, nums):
3        x=[]
4        for i in range(len(nums)):
5            y=[]
6            s=str(nums[i])
7            for ch in s:
8                y.append(int(ch))
9            x.append(max(y))
10        t=[]
11        x=list(set(x))
12        for i in range(len(x)):
13            
14            p=[]
15            for j in range(len(nums)):
16                if str(x[i])==max(str(nums[j])):
17                    
18                    p.append(nums[j])
19            if len(p)>1:
20                t.append(p)
21        if(len(t)==0):
22            return(-1)
23        else:
24            z=[]
25            for i in range(len(t)):
26                t[i].sort(reverse=True)
27                z.append(t[i][0]+t[i][1])
28            return(max(z))