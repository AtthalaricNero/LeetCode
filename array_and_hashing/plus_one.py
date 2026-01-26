# Problem
# Given a large integer represented as an array of digits, increment the integer by one and return the resulting array of digits.

# Definition
# The input digits is a list of integers, where each element represents a single digit of the integer.
# The digits are ordered from most significant to least significant (left-to-right).
# The integer does not contain leading zeros.
# Increment the integer by exactly 1.

# Notes
# Each element in digits is in the range 0–9.
# Be careful with carry-over when a digit becomes 10.
# For example, [9] becomes [1,0].
# The input array can have a length up to 100.
# Common approaches:
# Convert the list of digits to an integer, add one, and convert back to a list (simpler but may not scale for very large integers).
# Simulate addition from the least significant digit to the most significant, handling carry manually (preferred for interviews).

# Return
# Return a list of integers representing the new number after incrementing by one.
# The returned list should maintain most significant to least significant order.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0        
        for n in digits:
            result = result * 10 + n
        
        result += 1
        
        return list(map(int, str(result)))

if __name__ == "__main__":
    nums = [9]
    
    sol = Solution()
    
    print(sol.plusOne(nums))
    
