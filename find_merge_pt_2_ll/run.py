
def FindMergeNode(nodeA, nodeB):

    nodes_visited = set()

    while(nodeA):
        nodes_visited.add(nodeA)
        nodeA = nodeA.next

    while(not nodeB in nodes_visited):
        nodeB = nodeB.next

    return nodeB.data

