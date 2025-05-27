from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        first = head
        second = head.next

        first.next = self.swapPairs(second.next)

        second.next = first
        return second


def print_list(list_node: ListNode):
    while list_node != None:
        print(list_node.val)
        list_node = list_node.next


list1_head = ListNode(1)
curr = list1_head
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(5)

sol = Solution()
print_list(sol.swapPairs(list1_head))