# Last updated: 5/25/2026, 11:13:11 AM
1class Solution(object):
2    def toGoatLatin(self, sentence):
3        x=sentence.split()
4        z=["a","e","i","o","u","A","E","I","O","U"]
5        for i in range(len(x)):
6            if x[i][0] in z:
7                x[i]=x[i]+"ma"+(i+1)*"a"
8            else:
9                t=x[i][0]
10                x[i]=x[i].replace(x[i][0],"",1)
11                x[i]=x[i]+t+"ma"+(i+1)*"a"
12        return " ".join(x)