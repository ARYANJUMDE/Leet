# Last updated: 10/26/2026, 12:11:04 PM
1class Solution(object):
2    def asteroidCollision(self, asteroids):
3        x=[]
4        for i in range(len(asteroids)):
5            if(asteroids[i]>0 and len(x)>0 and x[-1]<0) or (asteroids[i]<0 and len(x)>0 and x[-1]>0):
6                j=-1
7                while len(x)>0:
8                    if x[j]<0:
9                        x.append(asteroids[i])
10                        break
11                    if abs(x[j])==abs(asteroids[i]):
12                        x.pop()
13                        break
14                    if abs(x[j])>abs(asteroids[i]):
15                        break
16                    else:
17                        x.pop()
18                        if len(x)==0:
19                            x.append(asteroids[i])
20                            break
21            elif asteroids[i]>0:
22                x.append(asteroids[i])
23            elif (asteroids[i]<0 and len(x)==0) or (asteroids[i]<0 and x[-1]<0):
24                x.append(asteroids[i])
25        return(x)
26
27        