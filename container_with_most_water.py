'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


'''

class Solution_1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) -1 
        prev_start = 0
        prev_end = 0
        result = 0
        
        while start != end:
            
            if height[start] < prev_start:
                start += 1
                continue
                
            if height[end] < prev_end:
                end -= 1
                continue
                
            new_container = min(height[start], height[end]) * (end - start)
            
            if new_container > result:
                result = new_container
                
            if height[start] < height[end]:
                prev_start = height[start]
                start += 1
            else:
                prev_end = height[end]
                end -= 1
                
        return result

class Solution_2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) -1 
        area = 0
        prev_start = 0
        prev_end = 0
        
        while start != end:
            
            if height[start] < prev_start:
                start += 1
                continue
                
            if height[end] < prev_end:
                end -= 1
                continue
            
            area = max(area, (end - start) * min(height[start], height[end]))
                       
            if height[start] < height[end]:
                prev_start = height[start]
                start += 1
            else:
                prev_end = height[end]
                end -= 1
                
        return area
        
# BRUTE FORCE
class Solution_3(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = 1 
        area = 0
        
        for start in range(len(height)):
            for end in range(start+1, len(height)):
                area = max(area, (end-start)*min(height[start], height[end]))
                
        return area
