# Last updated: 12/27/2025, 6:56:59 PM
class Solution(object):
    def calPoints(self, operations):
        sum1=0
        l=[]
        for op in operations:
            if(op!="C" and op!="D" and op!="+"):
                l.append(int(op))
            if(op=="+"):
                sum1=l[-1]+l[-2]
                l.append(sum1)
            if(op=="C"):
                l.remove(l[-1])

            if(op=="D"):
                l.append(2*l[-1])
        return(sum(l))

        