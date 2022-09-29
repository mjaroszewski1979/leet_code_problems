'''
Given the root of a binary tree, invert the tree, and return its root.

 
Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecursive(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

import collections

class SolutionIterative(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = collections.deque([root])
        
        while len(q):
            
            current = q.popleft()
            
            if current is None:
                continue
                
            temp = current.left
            current.left = current.right
            current.right = temp
            
            q.append(current.left)
            q.append(current.right)
            
        return root