class Solution:
    def partition(self, head, x):
        before = ListNode(0)
        after = ListNode(0)

        b = before
        a = after

        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                a.next = head
                a = a.next

            head = head.next

        a.next = None
        b.next = after.next

        return before.next