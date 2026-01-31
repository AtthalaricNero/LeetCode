from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        pointer3 = (m + n) - 1
        
        while pointer2 >= 0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
              nums1[pointer3] = nums1[pointer1]
              pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -=1
            pointer3 -=1  
        
if __name__ == "__main__":
    nums1 = [0]
    nums2 = [1]
    
    sol = Solution()
    
    sol.merge(nums1, 0 , nums2, 1)