# Problem:
# Given the head of a singly linked list, determine whether the list contains a cycle.

# Definition:
# A linked list has a cycle if, by following the `next` pointers, at least one node
# can be visited more than once (i.e., the list loops instead of ending at null).

# Notes:
# - The `index` mentioned in the problem description is ONLY for test case construction.
# - In the actual implementation, we are NOT given the index or cycle position.
# - We only have access to the `head` node.
# - The task is to detect whether a cycle exists, not where it starts.

# Return:
# - true  -> if a cycle exists
# - false -> if the list terminates at null

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer: return True
            
        return False
    
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    head = node1
    
    sol = Solution()
    
    print(sol.hasCycle(head))
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    
    head = node1
    
    print(sol.hasCycle(head))
    