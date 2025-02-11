def reverse(x: int) -> int:
    ans = 0
    neg = x < 0  # Check if x is negative
    x = abs(x)   # Work with absolute value

    while x > 0:
        rem = x % 10  # Extract last digit
        ans = ans * 10 + rem  # Build reversed number
        x //= 10  # Remove last digit

    if neg:
        ans = -ans  # Restore negative sign

    # Check for 32-bit signed integer overflow
    if ans < -2**31 or ans > 2**31 - 1:
        return 0  # Overflow condition

    return ans





# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 
# 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1
