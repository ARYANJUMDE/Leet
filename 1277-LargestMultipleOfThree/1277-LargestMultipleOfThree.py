# Last updated: 12/27/2025, 6:56:39 PM
class Solution(object):
    def largestMultipleOfThree(self, digits):
        # Sort digits in descending order for largest number
        digits.sort(reverse=True)
        
        # Buckets to store digits by remainder when divided by 3
        mod_buckets = {0: [], 1: [], 2: []}
        total = 0
        
        for d in digits:
            mod_buckets[d % 3].append(d)
            total += d
        
        remainder = total % 3
        
        # Function to remove smallest digit(s) to fix remainder
        def remove_digits(rem):
            if rem == 1:
                if mod_buckets[1]:
                    digits.remove(min(mod_buckets[1]))
                elif len(mod_buckets[2]) >= 2:
                    smallest_two = sorted(mod_buckets[2])[:2]
                    digits.remove(smallest_two[0])
                    digits.remove(smallest_two[1])
                else:
                    return False
            elif rem == 2:
                if mod_buckets[2]:
                    digits.remove(min(mod_buckets[2]))
                elif len(mod_buckets[1]) >= 2:
                    smallest_two = sorted(mod_buckets[1])[:2]
                    digits.remove(smallest_two[0])
                    digits.remove(smallest_two[1])
                else:
                    return False
            return True
        
        if remainder != 0:
            if not remove_digits(remainder):
                return ""
        
        if not digits:
            return ""
        
        # Handle case where all digits are zeros
        if digits[0] == 0:
            return "0"
        
        # Join digits to form the largest number
        return "".join(map(str, digits))

        