
def Reverse(next_node):

    prev_node = None
    
    while(next_node):
        next_node.prev = next_node.next
        next_node.next = prev_node
        prev_node = next_node
        next_node = next_node.prev

    return prev_node

