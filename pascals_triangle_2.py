'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[] for i in range(rowIndex+1)]
        
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j < i:
                    if j == 0:
                        result[i].append(1)
                    else:
                        result[i].append(result[i-1][j] + result[i-1][j-1])
                        
                elif i == j:
                    result[i].append(1)
                    
        return result[rowIndex]