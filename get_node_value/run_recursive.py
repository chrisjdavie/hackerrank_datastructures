
def _GetNode(node, position):
    if not node:
        return None, 0

    value, index = _GetNode(node.next, position)

    if index == position:
        value = node.data
    
    index += 1

    return value, index
    

def GetNode(head, position):
    return _GetNode(head, position)[0]

