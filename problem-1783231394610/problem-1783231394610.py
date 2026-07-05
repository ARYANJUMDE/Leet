# Last updated: 7/5/2026, 11:33:14 AM
1class Solution(object):
2    def intToRoman(self, num):
3        s = str(num).zfill(4)
4        t = ""
5        # Thousands
6        t = t + int(s[0]) * "M"
7        # Hundreds
8        if int(s[1]) == 9:
9            t += "CM"
10        elif int(s[1]) >= 5:
11            t += "D"
12            t += (int(s[1]) - 5) * "C"
13        elif int(s[1]) == 4:
14            t += "CD"
15        else:
16            t += int(s[1]) * "C"
17        # Tens
18        if int(s[2]) == 9:
19            t += "XC"
20        elif int(s[2]) >= 5:
21            t += "L"
22            t += (int(s[2]) - 5) * "X"
23        elif int(s[2]) == 4:
24            t += "XL"
25        else:
26            t += int(s[2]) * "X"
27        # Ones
28        if int(s[3]) == 9:
29            t += "IX"
30        elif int(s[3]) >= 5:
31            t += "V"
32            t += (int(s[3]) - 5) * "I"
33        elif int(s[3]) == 4:
34            t += "IV"
35        else:
36            t += int(s[3]) * "I"
37        
38        return(t)
39        