
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(self, head):
    if not head:
        return None
    pointer = head.next
    current = head
    while pointer is not None:
        # if current value is equal to the next one, link current to one even after and update the pointer to the new one
        if pointer.val == current.val:
            current.next = pointer.next
            pointer = pointer.next
        # otherwise just move one with both pointers
        else :
            current = current.next
            pointer = pointer.next

    return head