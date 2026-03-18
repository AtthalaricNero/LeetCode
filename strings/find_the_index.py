class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)

        for i in range(haystack_length - needle_length + 1):
            word = haystack[i : i + needle_length]
            if word == needle:
                return i
        
        return -1         
if __name__ == "__main__":
    strings = "alobogoba"
    key = "ba"
    
    sol = Solution()
    
    index = sol.strStr(strings, key)
    
    print(index)