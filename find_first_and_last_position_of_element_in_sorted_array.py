'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        first = 0
        last = 0
        
        if target not in nums or len(nums) == 0:
            return [-1, -1]
        elif nums.count(target) == 1:
            idx = nums.index(target)
            res = [idx, idx]
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    res.append(i)
            res = [res[0], res[-1]]
        return res
                