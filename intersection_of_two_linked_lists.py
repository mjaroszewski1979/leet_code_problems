'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
Note that the linked lists must retain their original structure after the function returns.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        inter = set()
        
        while headA:
            inter.add(headA)
            headA = headA.next
            
        while headB:
            if headB in inter:
                return headB
            headB = headB.next
            
        return None