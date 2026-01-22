# Problem
# Given an array nums of unique integers, generate all possible subsets of nums.

# Definition
# A subset is any combination of elements taken from nums.
# Each element has two choices: included or not included.
# Total subsets = 2^n, where n = len(nums).

# Notes
# All elements are unique meaning therea are no duplicate subsets
# Order of subsets does not matter
# Empty subset must be included
# Use backtracking / DFS with two choices at each index (take or skip)
# Base case: when index reaches len(nums)

# Return
# Return a list of all subsets in the form:
# List[List[int]]
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        
        def backtracking(n):
            if n == len(nums):
              result.append(subset.copy())
              return
            
            subset.append(nums[n])
            backtracking(n + 1)
            
            subset.pop()
            backtracking(n + 1)
        
        backtracking(0)
        
        return result

if __name__ == "__main__":
    numbers = [1, 2, 3]
    
    sol = Solution()
    
    print(sol.subsets(numbers)) # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]