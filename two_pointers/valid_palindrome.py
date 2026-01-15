# Problem:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return True if it is a palindrome, or False otherwise.

# Definition:
# Implement the function `isPalindrome(s: str) -> bool`
# - s: a string consisting only of printable ASCII characters
# - 1 <= len(s) <= 2 * 10^5

# Notes:
# - Uppercase letters should be converted to lowercase.
# - All non-alphanumeric characters should be ignored.
# - An empty string or a string with only non-alphanumeric characters is considered a palindrome.

# Return:
# - True  -> if the string is a palindrome
# - False -> otherwise
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_pointer = 0
        rear_pointer = len(s) - 1
        
        s = s.lower()
        
        while front_pointer < rear_pointer:
            if not s[front_pointer].isalnum():
                front_pointer = front_pointer + 1        
            elif not s[rear_pointer].isalnum():
                rear_pointer = rear_pointer - 1
            else:
                if s[front_pointer] != s[rear_pointer]:
                    return False
                else:
                    front_pointer = front_pointer + 1
                    rear_pointer = rear_pointer - 1
                    
        return True

if __name__ == "__main__":
    string = "Was it a car or a cat I saw?"
    string2 = " "
    string3 = "race a car"
    
    sol = Solution()
    
    print(sol.isPalindrome(string))
    print(sol.isPalindrome(string2))
    print(sol.isPalindrome(string3))
    