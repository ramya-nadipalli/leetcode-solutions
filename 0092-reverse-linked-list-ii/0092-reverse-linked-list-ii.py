class Solution:
    def reverseBetween(self, head, left, right):
        # Dummy node helps when left == 1
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before 'left'
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Start reversing
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next

            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next