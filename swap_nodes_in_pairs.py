'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution_1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while right and right.next:
            
            temp_1 = right.next.next
            temp_2 = right.next
            
            temp_2.next = right
            right.next = temp_1
            left.next = temp_2
            
            left = right
            right = temp_1
            
        return dummy.next

class Solution_2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        dummy = curr = ListNode()
        curr.next = head
        
        while curr.next and curr.next.next:
            left = curr.next
            right = curr.next.next
            curr.next = right
            left.next = right.next
            right.next = left
            curr = left
            
        return dummy.next


class Solution_3(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        if head is None or head.next is None:
            return head
        else:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp

class Solution_4(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        prev = dummy = ListNode(0, head)
        curr = head
        
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
            curr = curr.next
        return dummy.next