'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
RECURSIVE

'''
class Solution_1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def dfs(p,q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p) or p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p,q)

class Solution_2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution_3(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        
        if p and q:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False

'''
ITERATIVE 

'''
from collections import deque

class Solution_4(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        stack = deque()
        stack.append((p, q))

        
        while stack:
            p_curr, q_curr = stack.pop()
                
        
        
            if p_curr and q_curr:
                
                if (p_curr.val != q_curr.val) or (p_curr.left and not q_curr.left) or (q_curr.left and not p_curr.left):
                    return False
                
                if p_curr.left and q_curr.left:
                    stack.append((p_curr.left, q_curr.left))

                
                
                if p_curr.right and q_curr.right:
                    stack.append((p_curr.right, q_curr.right))
                    
                elif (p_curr.right and not q_curr.right) or (q_curr.right and not p_curr.right):
                    return False
                
            elif not p_curr or not q_curr:
                return False
            
        return True
            