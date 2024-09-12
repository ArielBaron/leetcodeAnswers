# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


def Main():
    def String_to_linked_list(s):
        head = ListNode(int(s[0]))
        current = head
        for char in s[1:]:
            new_node = ListNode(int(char))  # Create a new node for each digit
            current.next = new_node  # Link the current node to the new node
            current = new_node  # Move to the new node
        return head
    def add_two_linked_lists(l1, l2):
        current1 = l1
        current2 = l2
        S1, S2 = "", ""
        while current1:
            S1 += str(current1.val)
            current1 = current1.next
        while current2:
            S2 += str(current2.val)
            current2 = current2.next
        n1,n2 = int(S1[::-1]),int(S2[::-1])
        return String_to_linked_list(str(n1+n2))

    return add_two_linked_lists(l1, l2)


Main()
