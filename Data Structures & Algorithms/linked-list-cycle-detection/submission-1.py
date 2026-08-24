# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        values=set()
        list1=head
        while list1:
            if list1 in values:
                return True
            values.add(list1)
            list1=list1.next
        return False