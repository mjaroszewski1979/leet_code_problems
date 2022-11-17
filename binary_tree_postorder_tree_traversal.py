'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        def inorder(root):
            if not root:
                return
            
            
            inorder(root.left)
            inorder(root.right)
            res.append(root.val)
            
        inorder(root)
        return res

from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        
        
        
        if not root:
            return None
        
        result = []
        stack = deque()
        stack.append(root)
        current = None
        
        while stack:
            previous = current
            current = stack.pop()
            
            if previous and ((previous is current) or (previous is current.left) or (previous is current.right)):
                result.append(current.val)
            
            else:
                stack.append(current)
                
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return result