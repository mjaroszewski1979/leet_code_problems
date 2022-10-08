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

class Solution_1(object):
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

class Solution_2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pointer_1 = headA
        pointer_2 = headB
        
        while pointer_1 != pointer_2:
            if pointer_1:
                pointer_1 = pointer_1.next
            else:
                pointer_1 = headB
                
            if pointer_2:
                pointer_2 = pointer_2.next
            else:
                pointer_2 = headA
                
        return pointer_1