# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(self, list1, list2):
    # edge case one empty or both empty
    if (list1 == None) and list2 == (None):
        return None
    elif list1 == None:
        return list2
    elif list2 == None :
        return list1 
    
    # Create a third list
    list3 = None

    # We keep the first list and change that
    # This are the iters
    l1_pointer = list1
    l2_pointer = list2
    l3_pointer = list3

    while l1_pointer is not None or l2_pointer is not None:

        # This two are made when a list is finished
        if l1_pointer is None:
            l3_pointer.next = ListNode(val=l2_pointer.val)
            l3_pointer = l3_pointer.next
            l2_pointer = l2_pointer.next
            continue
        if l2_pointer is None:
            l3_pointer.next = ListNode(val=l1_pointer.val)
            l3_pointer = l3_pointer.next
            l1_pointer = l1_pointer.next
            continue

        if l1_pointer.val < l2_pointer.val:
            if list3 is None:
                list3 = ListNode(val=l1_pointer.val)
                l3_pointer = list3
                l1_pointer = l1_pointer.next
                continue

            l3_pointer.next = ListNode(val=l1_pointer.val)
            l3_pointer = l3_pointer.next 
            l1_pointer = l1_pointer.next 
            
        else :
            if list3 is None:
                list3 = ListNode(val=l2_pointer.val)
                l3_pointer = list3
                l2_pointer = l2_pointer.next
                continue

            l3_pointer.next = ListNode(val=l2_pointer.val)
            l3_pointer = l3_pointer.next 
            l2_pointer = l2_pointer.next 

    return list3
    



             
        