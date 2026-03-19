# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            if slow_ptr == fast_ptr:
                ptr = head
                while slow_ptr != ptr:
                    ptr = ptr.next
                    slow_ptr = slow_ptr.next
                
                return ptr

        return None
    
if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    head = node1
    
    sol = Solution()
    
    print(sol.detectCycle(head))