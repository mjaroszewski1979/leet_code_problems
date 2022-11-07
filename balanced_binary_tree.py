'''
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        
        def height(root):
            if root is None:
                return 0
            h_left = height(root.left)
            h_right = height(root.right)
            
            if h_left > h_right:
                return h_left + 1
            else:
                return h_right + 1
            
        if root is None:
            return True
        
        h_left = height(root.left)
        h_right = height(root.right)
        
        return (abs(h_left - h_right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)