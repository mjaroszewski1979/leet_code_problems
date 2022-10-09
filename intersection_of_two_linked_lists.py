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

class Solution_3(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        length_a = get_length(headA)
        length_b = get_length(headB)
        
        
        if length_a > length_b:
            diff = length_a - length_b
            pointer_long = headA
            pointer_short = headB
            
        else:
            diff = length_b - length_a
            pointer_long = headB
            pointer_short = headA
            
        i = 0
        while i < diff:
            i += 1
            pointer_long = pointer_long.next
            
        while pointer_long != pointer_short:
            pointer_long = pointer_long.next
            pointer_short = pointer_short.next
            
        return pointer_long