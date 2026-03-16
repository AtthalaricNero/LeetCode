from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        reader = 1
        
        while reader < len(nums):
            if nums[write] != nums[reader]:
                nums[write + 1] = nums[reader]
                write += 1
            reader += 1
        
        k = write + 1
                                
        return k
         
if __name__ == "__main__":
    arr = [1, 1, 1,2, 2,3, 3, 4]
    
    sol = Solution()
    
    k= sol.removeDuplicates(arr)
    
    print(f"k: {k}")
    
    for i in range(k):
        print(arr[i])       