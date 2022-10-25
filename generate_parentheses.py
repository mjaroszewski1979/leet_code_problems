'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''

class Solution(object):
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