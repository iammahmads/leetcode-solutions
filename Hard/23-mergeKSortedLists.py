from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = dict()

        for i in range(0, len(lists)):
            curr: ListNode | None = lists[i]
            while curr != None:
                counter[curr.val] = counter.get(curr.val, 0) + 1
                curr = curr.next

        head = ListNode(0)
        curr = head
        for key, value in sorted(counter.items()):
            for _ in range(value):
                curr.next = ListNode(key)
                curr = curr.next

        return head.next


    
def print_list(list_node: ListNode):
    while list_node != None:
        print(list_node.val)
        list_node = list_node.next


list1_head = ListNode(1)
curr = list1_head
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(5)

list2_head = ListNode(1)
curr = list2_head
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(4)

list3_head = ListNode(2)
curr = list3_head
curr.next = ListNode(6)

sol = Solution()
print_list(sol.mergeKLists([list1_head, list2_head, list3_head]))

        