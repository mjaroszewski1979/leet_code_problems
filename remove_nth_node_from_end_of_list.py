'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = right = head 
        
        for i in range(n):
            left = left.next
            
        if not left:
            return head.next
        
        while left.next:
            left = left.next
            right = right.next
            
        right.next = right.next.next
        
        return head

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = left = right = ListNode(0, next = head) 
        
        for _ in range(n):
            left = left.next
            
        
        while left.next:
            left = left.next
            right = right.next
            
        right.next = right.next.next
        
        return dummy.next