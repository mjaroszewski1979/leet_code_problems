'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

class Solution_1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        result = ''
        for char in s:
            if char.isalnum():
                result += char
        result = result.lower()
        return result == result[::-1]

class Solution_2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alpha(s[left]):
                left += 1
            while right > left and not self.is_alpha(s[right]):
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
                
        
    def is_alpha(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'))


class Solution_3(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub("[^a-z|^0-9]", "", s.lower())
        
        return s == s[::-1]