'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''



class Solution_1(object):

    def twoSum(self, nums, target):
        result = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in result:
                return [result[diff], index]
            result[num] = index
        return

class Solution_2(object):

    def twoSum(self, nums, target):
        result = {}
        for i in range(len(nums)):
            if nums[i] in result:
                return [result[nums[i]], i]
            result[target - nums[i]] = i
        return