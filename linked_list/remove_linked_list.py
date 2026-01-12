class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        current = head
        
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next

if __name__ == "__main__":
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(6)
    list.next.next.next = ListNode(3)
    list.next.next.next.next = ListNode(4)
    list.next.next.next.next.next = ListNode(5)
    list.next.next.next.next.next.next = ListNode(6)
    
    sol = Solution()
    result = sol.removeElements(list, 6)
    
    while result is not None:
        print(result.val)
        result = result.next