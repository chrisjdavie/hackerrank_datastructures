
def inOrder(node):
    
    order = _in_order(node)
    print(*order)


def _in_order(node):

    order = []    
    stack = [node]
    visited = set()

    while stack:
        a_node = stack.pop()
        if not a_node:
            continue

        if a_node in visited:
            order.append(a_node.data)
        else:
            visited.add(a_node)
            stack.append(a_node.right)
            stack.append(a_node)
            stack.append(a_node.left)

    return order
