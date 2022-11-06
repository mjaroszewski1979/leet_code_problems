'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution_1(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: return None
        
        temp = []
        
        while head:
            temp.append(head.val)
            head = head.next
            
        def recursive(temp):
            if not temp:
                return None
            else:
                mid = len(temp) // 2
                root = TreeNode(temp[mid])
                root.left = recursive(temp[:mid])
                root.right = recursive(temp[mid+1:])
            return root
        
        return recursive(temp)


class Solution_2(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: return None
        
        
        length = 0
        self.head = head
        
        while head:
            length += 1
            head = head.next
            
        def recursive(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            left = recursive(start, mid-1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = recursive(mid+1, end)
            return root
        
        return recursive(0, length -1)