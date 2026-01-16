# Last updated: 1/16/2026, 3:08:31 PM
# Pseudocode
if dividend == -2147483648 and divisor == -1:
    return 2147483647
sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
dividend, divisor = abs(dividend), abs(divisor)
result = 0
while dividend >= divisor:
    # Find largest multiple (e.g., 3 * 8 = 24) using left shifts
    temp, count = divisor, 1
    while dividend >= (temp << 1):
        temp <<= 1
        count <<= 1
    dividend -= temp
    result += count
return sign * result