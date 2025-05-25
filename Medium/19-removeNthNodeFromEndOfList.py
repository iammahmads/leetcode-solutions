from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        list_length = 0
        while curr != None:
            list_length += 1
            curr = curr.next
            
        # check if the node to be removed is head
        if list_length - n == 0:
            head = head.next
            return head
        
        curr = head
        prev = None 
        i = 0
        while i < list_length:
            if list_length - n == i:
                prev.next = curr.next
                break
                
            prev = curr
            curr = curr.next
            i += 1
                    
        return head


def print_list(head : Optional[ListNode]):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next
             
sol = Solution()
head = ListNode(1)
# curr = head
# curr.next = ListNode(2)
# curr = curr.next
# curr.next = ListNode(3)
# curr = curr.next
# curr.next = ListNode(4)
# curr = curr.next
# curr.next = ListNode(5)
# curr = curr.next

print(print_list(sol.removeNthFromEnd(head, 1)))
            