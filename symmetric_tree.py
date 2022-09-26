'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''def isMirror(left,right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            else:
                return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right,right.left)
        
        return isMirror(root, root)'''
        
        if root is None:
            return True
        
        stack = []
        if root.left and root.right:
            stack.append(root.left)
            stack.append(root.right)
            
        while stack:
            right = stack.pop()
            left = stack.pop()
            
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
            
        return True