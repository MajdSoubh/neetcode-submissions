class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        node = head

        while (node is not None):
            next = node.next
            node.next = previous_node
            previous_node = node
            node = next
        return previous_node