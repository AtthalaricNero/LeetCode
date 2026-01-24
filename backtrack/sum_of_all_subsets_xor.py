from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        
        def backtracking(n, current):
            nonlocal result
            if n == len(nums):
                result += current
                return
            
            backtracking(n + 1, current ^ nums[n])
            
            backtracking(n + 1, current)
        
        backtracking(0, 0)
        return result
    
if __name__ == "__main__":
    numbers = [5, 1, 6]
    
    sol = Solution()
    
    print(sol.subsetXORSum(numbers))