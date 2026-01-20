# Problem:
# Given a 1-indexed array of integers 'numbers' sorted in non-decreasing order,
# find two numbers such that they add up to a specific 'target' number.
# Return their indices as a list [index1, index2], where 1 <= index1 < index2 <= len(numbers).
# Only one solution exists and you may not use the same element twice.

# Definition:
# We define a function twoSum(numbers: List[int], target: int) -> List[int]
# that takes a sorted list of integers and a target integer, and returns
# a list of two indices (1-indexed) of the numbers that sum up to the target.

# Notes:
# - Use two-pointer technique for O(n) time complexity.
# - Constant extra space is required (no additional data structures).
# - The array is already sorted, so we can move pointers inward based on sum comparison.

# Return Comment:
# Return a list of two integers [index1, index2] representing the positions
# of the numbers in 'numbers' that add up to 'target'. Indices are 1-based.
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front_pointer = 0
        rear_pointer = len(numbers) - 1
        
        while front_pointer < rear_pointer:
            if numbers[front_pointer] + numbers[rear_pointer] < target:
              front_pointer += 1
            elif numbers[front_pointer] + numbers[rear_pointer] > target:
                rear_pointer -= 1
            else:
                return [(front_pointer + 1),(rear_pointer + 1)]
            
if __name__ == "__main__":
    num = [2, 7, 11, 15]
    
    sol = Solution()
    
    print(sol.twoSum(num, 9))