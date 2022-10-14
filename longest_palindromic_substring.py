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


class Solution_3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palindrome(left,right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ''
        for i in range(len(s)):
            
            temp = get_palindrome(i, i)
            if len(temp) > len(result):
                result = temp
                
            temp = get_palindrome(i, i+1)
            if len(temp) > len(result):
                result = temp
                
        return result

class Solution_4(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palindrome(s, left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ''
        
        for i in range(len(s)):
            
            odd = get_palindrome(s, i, i)
            
            even = get_palindrome(s, i, i+1)
            
            result = max(odd, even, result, key=len)
            
        return result

class Solution_5(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palindrome(s):
            return (s == s[::-1])
        
        longest = s[0]
        step = len(longest) // 2
        
        # single letter center
        for center in range(1, len(s)-1):
            bounds = [center-(1+step), center+(1+step)]
            while(bounds[0] > -1 and bounds[1] < len(s)):
                if get_palindrome(s[bounds[0]:bounds[1]+1]):
                    longest = s[bounds[0]:bounds[1]+1]
                    step = len(longest) // 2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break
        # double letter center      
        for center in range(step, len(s)-step-1):
            bounds = [center-(step), center+(1+step)]
            while(bounds[0] > -1 and bounds[1] < len(s)):
                if get_palindrome(s[bounds[0]:bounds[1]+1]):
                    longest = s[bounds[0]:bounds[1]+1]
                    step = len(longest) // 2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break
                    
        return longest