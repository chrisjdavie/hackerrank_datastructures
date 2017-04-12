
def RemoveDuplicates(head):
    if not head:
        return head

    last_uniq_node = head
    next_node = head.next

    while(next_node):
        
        if next_node.data != last_uniq_node.data:
            last_uniq_node.next = next_node
            last_uniq_node = next_node

        next_node = next_node.next

    last_uniq_node.next = None

    return head

