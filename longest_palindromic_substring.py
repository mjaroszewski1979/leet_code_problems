'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''

class Solution_1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        res_len = 0
        
        for i in range(len(s)):
            
            left, right = i, i          
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
                
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
            
        return res


class Solution_2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palindrome(s):
            return (s == s[::-1])
        
        for length in range(len(s), 0, -1):
            for start_index in range(0, len(s)+1-length):
                if get_palindrome(s[start_index:(start_index+length)]):
                    return s[start_index:(start_index+length)]