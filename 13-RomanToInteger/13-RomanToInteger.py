# Last updated: 12/27/2025, 6:58:26 PM
class Solution(object):
    def romanToInt(self, s):
        num=0
        if("IV" in s):
            num=num+4
            s=s.replace("IV","")
        if("IX" in s):
            num=num+9
            s=s.replace("IX","")
        if("XL" in s):
            num=num+40
            s=s.replace("XL","")
        if("XC" in s):
            num=num+90
            s=s.replace("XC","")
        if("CD" in s):
            
            num=num+400
            s=s.replace("CD","")
        if("CM" in s):
            num=num+900
            s=s.replace("CM","")
        for ch in s:
            if(ch=="I"):
                num=num+1
            elif(ch=="V"):
                num=num+5
            elif(ch=="X"):
                num=num+10
            elif(ch=="L"):
                num=num+50
            elif(ch=="C"):
                num=num+100
            elif(ch=="D"):
                num=num+500
            elif(ch=="M"):
                
                num=num+1000
        return num

        