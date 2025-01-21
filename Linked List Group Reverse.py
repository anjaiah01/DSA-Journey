class Solution:

    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        curr = head
        newHead = None
        tail = None

        while curr is not None:
            groupHead = curr
            prev = None
            nextNode = None
            count = 0

            # Reverse the nodes in the current group
            while curr is not None and count < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1

            # If newHead is None, set it to the last node of the first group
            if newHead is None:
                newHead = prev

            # Connect the previous group to the current reversed group
            if tail is not None:
                tail.next = prev

            # Move tail to the end of the reversed group
            tail = groupHead

        return newHead





# Given the head a linked list, the task is to reverse every k node in the linked list. 
# If the number of nodes is not a multiple of k then the left-out nodes in the end, 
# should be considered as a group and must be reversed.
