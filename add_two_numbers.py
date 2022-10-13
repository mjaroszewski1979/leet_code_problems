'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode()
        current = temp
        
        carry = 0
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            res = val_1 + val_2 + carry
            carry = res // 10
            res = res % 10
            current.next = ListNode(res)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next

class Solution_2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = ''
        num_2 = ''
        
        while l1:
            num_1 = str(l1.val) + num_1
            l1 = l1.next
            
        while l2:
            num_2 = str(l2.val) + num_2
            l2 = l2.next
            
        if not num_1: num_1 = '0'
        if not num_2: num_2 = '0'
            
        result = int(num_1) + int(num_2)
        
        dummy = current = ListNode()
        
        for i in reversed(str(result)):
            current.next = ListNode(int(i))
            current = current.next
            
        return dummy.next

class Solution_3(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current = ListNode()
        carry = 0
        
        while l1 or l2:
            num = carry
            
            if l1 and l2:
                num += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
                
            elif l1:
                num += l1.val
                l1 = l1.next
                
            elif l2:
                num += l2.val
                l2 = l2.next
                
            carry = num // 10
            current.next = ListNode(num%10)
            current = current.next
            
        if carry == 1:
            current.next = ListNode(1)
                
        return dummy.next

class Solution_4(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(val = (l1.val + l2.val)%10)
        carry_over = (l1.val + l2.val) // 10
        current = result
        
        while(l1.next and l2.next):
            
            l1 = l1.next
            l2 = l2.next
            
            current.next = ListNode(val = (carry_over + l1.val + l2.val)%10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current = current.next
            
        while(l1.next):
            
            l1 = l1.next
            current.next = ListNode(val = (carry_over + l1.val)%10)
            carry_over = (carry_over + l1.val) // 10
            current = current.next
            
        while(l2.next):
            
            l2 = l2.next
            current.next = ListNode(val = (carry_over + l2.val)%10)
            carry_over = (carry_over + l2.val) // 10
            current = current.next
            
        if carry_over > 0:
            current.next = ListNode(val = 1)
            
        return(result)
            