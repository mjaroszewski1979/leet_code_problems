'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''

class Solution_1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index -1]:
                continue
                
            start = index + 1
            end = len(nums) - 1
            
            while start < end:
                current_sum = value + nums[start] + nums[end]
                if current_sum > 0:
                    end -= 1
                elif current_sum < 0:
                    start += 1
                else:
                    result.append([value, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                        
        return result

class Solution_2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        result = []
        nums = sorted(nums)
        
        for i in range(0, len(nums) - 2):
            
            if nums[i] > 0:
                break
                
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                
                temp = nums[i] + nums[start] + nums[end]
                
                if temp == 0:
                    result.append((nums[i], nums[start], nums[end]))
                if temp <= 0:
                    start += 1
                    while (nums[start] == nums[start-1]) and start < end:
                        start += 1
                else:
                    end -= 1
                    
        return result


class Solution_3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        result = []
        nums = sorted(nums)
        
        for i in range(0, len(nums) - 2):
            
            if nums[i] > 0:
                break
                
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                
                temp = nums[i] + nums[start] + nums[end]
                
                if temp == 0:
                    result.append((nums[i], nums[start], nums[end]))
                    start += 1
                elif temp < 0:
                    start += 1
                else:
                    end -= 1
                    
        return list(set(result))