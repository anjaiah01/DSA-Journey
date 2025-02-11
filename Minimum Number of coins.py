def minPartition(N):
    # List of Indian currency denominations sorted in descending order
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    # List to store the result (minimum coins/notes required)
    coins = []

    # Iterate through each denomination
    for coinVal in denominations:
        # Use as many of the current denomination as possible
        while N >= coinVal:
            coins.append(coinVal)  # Add the denomination to the result list
            N -= coinVal  # Reduce the remaining amount

    return coins  # Return the list of required denominations

# Example Usage:
N = 43
print(minPartition(N))  # Output: [20, 20, 2, 1]




# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 


# Example 1:

# Input: N = 43
# Output: 20 20 2 1
# Explaination: 
# Minimum number of coins and notes needed 
# to make 43. 

# Example 2:

# Input: N = 1000
# Output: 500 500
# Explaination: minimum possible notes
# is 2 notes of 500.

# Your Task:
# You do not need to read input or print anything. Your task is to complete the function minPartition()
#which takes the value N as input parameter and returns a list of integers in decreasing order.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


# Constraints:
# 1 ≤ N ≤ 106
