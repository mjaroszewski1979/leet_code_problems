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
class Solution_1(object):
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

class Solution_2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        
        def height(node):
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.result = max(self.result, (left_height + right_height))
            
            return max(left_height, right_height) + 1
        
        height(root)
        
        return self.result

class Solution_3(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        
        def height(root):
            if not root:
                return -1
            left = height(root.left)
            right = height(root.right)
            self.result = max(self.result, (left + right + 2))
            
            return max(left, right) + 1
        
        height(root)
        
        return self.result

class Solution_4(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.dfs(root)
        
        return self.ans
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.ans = max(self.ans,right+left)
        
        return max(left+1,right+1)