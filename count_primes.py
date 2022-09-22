'''
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

'''

'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 or n == 1: return 0
        
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        
        i = 2
        
        while i < n:
            tmp = i
            if primes[i]:
                tmp += i
                while tmp < n:
                    primes[tmp] = 0
                    tmp += i
                    
            i += 1
            
        return sum(primes)
        
'''