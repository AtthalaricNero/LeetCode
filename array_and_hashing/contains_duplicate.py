class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        
        for x in nums:
            if x in s:
                return True
            s.add(x)

        return False
    
if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3, 3]
    
    sol = Solution()
    
    result = sol.containsDuplicate(arr)
    
    print(result)