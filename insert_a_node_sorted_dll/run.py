
from linked_list_testing.double_node import Node

def SortedInsert(head, data):

    prev_node = None
    next_node = head

    while(next_node and next_node.data < data):
        prev_node = next_node
        next_node = next_node.next

    new_node = Node(data)

    new_node.prev = prev_node
    if prev_node:
        prev_node.next = new_node
    else:
        head = new_node

    new_node.next = next_node
    if next_node:
        next_node.prev = new_node

    return head

