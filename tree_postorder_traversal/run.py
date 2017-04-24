
def _post_order(node, output):

    if node:
        output = _post_order(node.left, output)
        output = _post_order(node.right, output)
        output.append(node.data)

    return output

def postOrder(root):

    tree_data = _post_order(root, [])
    
    print(*tree_data)

