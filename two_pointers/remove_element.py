from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0
        reader = 0
        
        while reader < len(nums):
            if nums[reader] != val:
              nums[writer] = nums[reader]
              writer += 1
            reader += 1
        
        k = writer
        
        return k
        
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    
    sol = Solution()
    
    k = sol.removeElement(nums, val)
    
    print(f"k: {k}")
    
    for i in range(k):
        print(nums[i])