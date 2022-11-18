'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
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
class Solution_1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res

from collections import deque
class Solution_2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        stack = deque()
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result

from collections import deque
class Solution_3(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        stack = deque()
        stack.append(root)
        current = root
        
        while current.left != None:
            stack.append(current.left)
            current = current.left 
            
        while stack:
            current = stack.pop()
            result.append(current.val)
            
            if current.right != None:
                stack.append(current.right)
                current = current.right
                
                while current.left != None:
                    stack.append(current.left)
                    current = current.left 
                    
        return result