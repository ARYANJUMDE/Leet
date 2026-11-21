# Last updated: 11/21/2026, 11:26:38 AM
1class Solution(object):
2    def asteroidsDestroyed(self, mass, asteroids):
3        asteroids.sort()
4        t=max(asteroids)
5        for i in range(len(asteroids)):
6            if mass>=asteroids[i]:
7                mass=mass+asteroids[i]
8            elif mass>=t:
9                return True
10            else:
11                return False
12        return True
13        