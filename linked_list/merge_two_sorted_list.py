class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
                
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
            
        
if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    
    sol = Solution()
    
    result = sol.mergeTwoLists(list1, list2)
    
    while result is not None:
        print(result.val)
        result = result.next