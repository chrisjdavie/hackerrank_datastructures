
def _pre_order(node):
    order = [ ]
    
    if node:
        order.append(node.data)
        order += _pre_order(node.left)
        order += _pre_order(node.right)

    return order


def preOrder(root):
    
    order = _pre_order(root)
    
    print(*order)

