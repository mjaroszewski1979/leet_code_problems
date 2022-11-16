'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        def inorder(root):
            if not root:
                return
            
            res.append(root.val)
            inorder(root.left)
            inorder(root.right)
            
        inorder(root)
        return res
from collections import deque

class Solution_2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        
        res = []
        q = deque()
        q.append(root)
        
        while q:
            node = q.pop()
            
            res.append(node.val)
            
            if node.right:
                q.append(node.right)
            
            if node.left:
                q.append(node.left)
            
        return res

class Solution_3(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        
        res = []
        q = deque()
        q.append(root)
        
        node = root
        
        while q:
            if node:
                res.append(node.val)
            
                if node.right:
                    q.append(node.right)
                
                node = node.left
            
            else:
                node = q.pop()

        return res