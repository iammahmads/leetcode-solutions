from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        
        if list1 == None:
            new_node = list2
            return new_node
        elif list2 == None:
            new_node = list1
            return new_node
        
        if list1.val < list2.val:
            new_node = list1
            list1 = list1.next
        else:
            new_node = list2
            list2 = list2.next

        head = new_node
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                new_node.next = list1
                list1 = list1.next
            else:
                new_node.next = list2
                list2 = list2.next
            new_node = new_node.next
                
        while list1 != None:
            new_node.next = list1
            list1 = list1.next
            new_node = new_node.next
        while list2 != None:
            new_node.next = list2
            list2 = list2.next
            new_node = new_node.next
            
        return head
    
    
def print_list(list_node: ListNode):
    while list_node != None:
        print(list_node.val)
        list_node = list_node.next
       
       
head1 = ListNode(1)
curr = head1
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(4)
curr = curr.next


head2 = ListNode(1)
curr = head2
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(4)
curr = curr.next
sol = Solution()
print_list(sol.mergeTwoLists(head1, head2))