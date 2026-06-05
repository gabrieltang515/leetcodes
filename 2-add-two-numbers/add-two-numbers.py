# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sum_node = ListNode(0)
        ptr = sum_node
        carry = 0

        while l1 != None or l2 != None:
            sum = 0
            if l1 == None:
                sum = l2.val + carry
            elif l2 == None: 
                sum = l1.val + carry
            else:
                sum = l1.val + l2.val + carry

            if len(str(sum)) > 1: # Means there is carry over
                ones = int(str(sum)[1])
                tens = int(str(sum)[0])
                sum_node.val = ones
                carry = tens
            else:
                sum_node.val = sum
                carry = 0

            if l1 != None: 
                l1 = l1.next
            
            if l2 != None:
                l2 = l2.next

            if l1 != None or l2 != None:
                sum_node.next = ListNode(0)
                sum_node = sum_node.next

        if carry > 0:
            sum_node.next = ListNode(carry)
            
        return ptr

