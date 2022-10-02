'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max((left_height + right_height), left_diameter, right_diameter)
    
    def height(self, root):
            
            if root is None:
                return 0
            return 1 + max(self.height(root.left), self.height(root.right))