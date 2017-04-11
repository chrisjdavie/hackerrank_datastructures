

def increment_node(node, prev_node):
    prev_node.next = node
    return node, node.next


def MergeLists(nodeA, nodeB):
    if not nodeA and not nodeB:
        return nodeA

    if not nodeB: 
        head = nodeA
        nodeA = nodeA.next
    elif not nodeA:
        head = nodeB
        nodeB = nodeB.next
    elif nodeA.data <= nodeB.data:
        head = nodeA
        nodeA = nodeA.next
    elif nodeB.data < nodeA.data:
        head = nodeB
        nodeB = nodeB.next

    prev_node = head

    while (nodeA and nodeB):
        if nodeA.data < nodeB.data:
            prev_node, nodeA = increment_node(nodeA, prev_node)
        else:
            prev_node, nodeB = increment_node(nodeB, prev_node)

    while nodeA:
        prev_node, nodeA = increment_node(nodeA, prev_node)

    while nodeB:
        prev_node, nodeB = increment_node(nodeB, prev_node)

    return head
