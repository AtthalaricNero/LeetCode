# Problem
# Given two strings s and t, determine whether t is an anagram of s.

# Definition
# An anagram is a string formed by rearranging the characters of another string so that both strings contain the same characters with the same frequencies, regardless of order.

# Notes
# The order of characters does not matter.
# Both strings must have the same length.
# Each character in s must appear the same number of times in t.
# Strings consist only of lowercase English letters.
# The problem can be solved by comparing character frequency counts.

# Return
# Return true if s and t are anagrams of each other.
# Otherwise, return false.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_freq = {}
        t_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
            
        if s_freq != t_freq:
            return False
        
        return True

if __name__ == "__main__":
    s1 = "bbcc"
    t1 = "ccbc"
    
    s2 = "racecar"
    t2 = "carrace"
    sol = Solution()
    
    print(sol.isAnagram(s1, t1))
    print(sol.isAnagram(s2, t2))