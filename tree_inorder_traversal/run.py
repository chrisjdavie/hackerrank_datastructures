
def _in_order(node, data_list):

    if node:
        data_list = _in_order(node.left, data_list)
        data_list.append(node.data)
        data_list = _in_order(node.right, data_list)

    return data_list


def inOrder(root):

    data_list = _in_order(root, [])

    print(*data_list)

