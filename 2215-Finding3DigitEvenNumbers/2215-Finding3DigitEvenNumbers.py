# Last updated: 12/27/2025, 6:56:19 PM
# from itertools import permutations
# class Solution(object):
#     def findEvenNumbers(self, digits):

#         # result=permutations(digits,3)
#         nums=[]
#         # for i in result:
#         #     print(i)
#         for i in permutations(digits,3):
#             if(i[0]!=0):
#                 num=int("".join(map(str,i)))
#                 if(num%2==0):

#                     nums.append(num)

#         # for j in range(len(nums)):

#         #     if(nums[j]%2==0 and nums[j] not in t):
#         #         t.append(nums[j])

#         # t.sort()     
#         # return(t)
#         return sorted(set(nums))

class Solution(object):
    def findEvenNumbers(self, digits):
        digits_count = [0]*10
        for d in digits:
            digits_count[d] += 1

        res = set()

        for d1 in range(1, 10):  # first digit cannot be 0
            if digits_count[d1] == 0:
                continue
            digits_count[d1] -= 1

            for d2 in range(0, 10):
                if digits_count[d2] == 0:
                    continue
                digits_count[d2] -= 1

                for d3 in [0, 2, 4, 6, 8]:  # must be even
                    if digits_count[d3] == 0:
                        continue
                    num = d1*100 + d2*10 + d3
                    res.add(num)

                digits_count[d2] += 1
            digits_count[d1] += 1

        return sorted(res)
      