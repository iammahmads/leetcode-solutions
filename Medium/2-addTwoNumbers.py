# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        carry = 0
        result = ListNode()
        current = result
        
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 != None  else 0
            val2 = l2.val if l2 != None  else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
            
        return result.next
        
        
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))))

sol = Solution()
sol.addTwoNumbers(l1=l1, l2=l2)