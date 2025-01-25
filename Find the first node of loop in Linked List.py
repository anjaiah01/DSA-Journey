class Solution:

    def findFirstNode(self, head):
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:

            # Move slow pointer by one step
            slow = slow.next

            # Move fast pointer by two steps
            fast = fast.next.next

            # Detect loop
            if slow == fast:

                # Move slow to head, keep
                # fast at meeting point
                slow = head

                # Move both one step at a time until
                # they meet
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                # Return the meeting node, which is the
                # start of the loop
                return slow

        # No loop found
        return None
