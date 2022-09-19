'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        def sum_of_squares(n):
            digits = str(n)
            res = []
            for digit in digits:
                res.append(pow(int(digit), 2))
            return sum(res)
        
        result = set()
        
        while n not in result:
            result.add(n)
            n = sum_of_squares(n)
            
            if n == 1:
                return True
            
        return False

'''
Using cycle detection algorithms such as the Floyd’s Tortoise and the Hare algorithm.

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        def sum_of_squares(n):
            n_sum = 0
            while (n != 0):
                temp = n % 10
                n_sum += (temp * temp)
                n = n // 10
            return n_sum
                
                
        
        if n == 1:
            return True
        else:
            slow = n
            fast = sum_of_squares(n)
            while (slow != fast):
                slow = sum_of_squares(slow)
                fast = sum_of_squares(fast)
                fast = sum_of_squares(fast)
                if slow == 1:
                    return True
            return False