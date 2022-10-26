'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''

class Solution_1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        result = []
        
        def recursive(left, right, stack, current):
            
            if left == right == 0:
                result.append(current)
                return
        
            if left > 0:
                recursive(left-1, right, stack+1, current+'(')
            if right > 0 and stack > 0:
                recursive(left, right-1, stack-1, current+')')
                
        recursive(n, n, 0, '')
        
        return result

from collections import deque

class Solution_2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        result = []
        stack = deque()
        
        def recursive(left, right):
            if left == right == n:
                result.append(''.join(stack))
                return
            
            if left < n:
                stack.append('(')
                recursive(left+1, right)
                stack.pop()
                
            if right < left:
                stack.append(')')
                recursive(left, right+1)
                stack.pop()
                
        recursive(0,0)
        return result

class Solution_3(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        result = []
        
        def recursive(left, right, temp, result):
            if left == 0 and right == 0:
                result. append(temp)
                return
            if left > 0:
                recursive(left-1, right, temp+'(', result)
            if right > left:
                recursive(left, right-1, temp+')', result)
                
        recursive(n, n, '', result)
        
        return result