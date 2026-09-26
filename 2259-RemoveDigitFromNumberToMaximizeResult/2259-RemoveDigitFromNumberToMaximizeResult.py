# Last updated: 9/26/2026, 4:15:24 PM
class Solution(object):
    def removeDigit(self, number, digit):
        x=[]
        y=[]
        for i in range(len(number)):
            if number[i]==digit:
                x.append(i)
        for i in range(len(x)):
            y.append(int(number[:x[i]]+""+number[x[i]+1:]))
        return str((max(y)))

        