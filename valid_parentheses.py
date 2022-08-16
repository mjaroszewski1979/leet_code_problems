'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def get_string(s):
            while len(s) > 0:
                if '()' in s:
                    s = s.replace('()', '')
                elif '[]' in s:
                    s = s.replace('[]', '')
                elif '{}' in s:
                    s = s.replace('{}', '')
                else:
                    return s
            return s
        
        if type(s) != str:
            return 'Please enter a valid input type!'
        elif (len(s)) % 2 != 0:
            return False
        else:
            result = get_string(s)
            if result == '':
                return True
            else:
                return False