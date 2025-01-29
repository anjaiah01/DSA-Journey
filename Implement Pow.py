class Solution:

    def power(self, b: float, e: int) -> float:
        # Base case: any number raised to the power of 0 is 1
        if e == 0:
            return 1.0

        # If the exponent is negative, compute the reciprocal
        if e < 0:
            return 1.0 / self.power(b, -e)

        # Recursively compute the power for half of the exponent
        half_power = self.power(b, e // 2)

        # If the exponent is odd, multiply by the base once more
        if e % 2 == 1:
            return b * half_power * half_power
        # If the exponent is even, square the half power
        else:
            return half_power * half_power


# Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

# Examples:

# Input: b = 3.00000, e = 5
# Output: 243.00000
