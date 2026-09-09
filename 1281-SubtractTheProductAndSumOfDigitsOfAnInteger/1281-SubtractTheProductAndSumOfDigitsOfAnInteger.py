# Last updated: 9/9/2026, 10:14:29 PM
class Solution(object):
    def subtractProductAndSum(self, n):
        x=[]
        for num in str(n):
            x.append(int(num))
        sum1=0
        pro=1
        for i in range(len(x)):
            sum1=sum1+x[i]
        for i in range(len(x)):
            pro=pro*x[i]
        return(pro-sum1)

        