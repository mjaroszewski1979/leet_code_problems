'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

from collections import deque

class Solution_1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        q = deque([(root, 1)])
        
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))