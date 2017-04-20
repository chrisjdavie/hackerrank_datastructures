
def _pre_order(node):
    order = [ node.data ]
    
    if node.left:
        order += _pre_order(node.left)
    
    if node.right:
        order += _pre_order(node.right)

    return order


def preOrder(root):
    
    if root:
        order = _pre_order(root)
    else:
        order = []
    
    for o in order:
        print(o)

