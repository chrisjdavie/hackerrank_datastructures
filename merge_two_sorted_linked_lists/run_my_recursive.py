# recursive solution, much less code. Perhaps a little harder to understand

def MergeLists(nodeA, nodeB):
    if not nodeA and not nodeB:
        return None
    if not nodeB: 
        return nodeA
    if not nodeA:
        return nodeB

    if nodeA.data < nodeB.data:
        next_node = nodeA
        nodeA = next_node.next
    else:
        next_node = nodeB
        nodeB = next_node.next

    next_node.next = MergeLists(nodeA, nodeB)
    return next_node

