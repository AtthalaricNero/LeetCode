class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'{': '}', '(': ')', '[': ']'}
        
        stack = []
        
        for char in s:
            if char in pair:
              stack.append(pair[char])
            else:
                if not stack:
                    return False
                if stack[-1] == char:
                  stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        
        return True
    
if __name__ == "__main__":
    input1 = '({)}'
    input2 = '{()}'
    input3 = '){}()'
    
    sol = Solution()
    
    print(sol.isValid(input1))
        
    print(sol.isValid(input2))
    
    print(sol.isValid(input3))