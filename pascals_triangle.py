'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

'''
class Solution_1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        result = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1])+1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
            
        return result

class Solution_2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        result = [[1]]
        
        for i in range(2, numRows+1):
            temp = [1]
            for j in range(1,i-1):
                temp.append(result[-1][j] + result[-1][j-1])
            temp.append(1)
            result.append(temp)
                
        return result

class Solution_3(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        
        result = [[] for i in range(numRows)]
        
        for i in range(numRows):
            for j in range(i+1):
                if j < i:
                    if j == 0:
                        result[i].append(1)
                    else:
                        result[i].append(result[i-1][j] + result[i-1][j-1])
                        
                elif i == j:
                    result[i].append(1)
                    
        return result