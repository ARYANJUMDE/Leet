# Last updated: 11/21/2026, 11:25:10 AM
1class Solution(object):
2    def asteroidsDestroyed(self, mass, asteroids):
3        asteroids.sort()
4        for i in range(len(asteroids)):
5            if mass>=asteroids[i]:
6                mass=mass+asteroids[i]
7            else:
8                return False
9        return True
10        