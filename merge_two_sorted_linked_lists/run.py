# recursive solution, much less code. Perhaps a little harder to understand
# 
# included features from hackerrank discussion. Less code again.
# 

def MergeLists(nodeA, nodeB):
    if not nodeA or not nodeB:
        return nodeA or nodeB

    if nodeA.data < nodeB.data:
        nodeA.next = MergeLists(nodeA.next, nodeB)
        return nodeA
    else:
        nodeB.next = MergeLists(nodeA, nodeB.next)
        return nodeB

