
class Node:

    def __init__(self, data, left = None, right = None):

        self.data = data
        self.left = left
        self.right = right


def swap_node(node, target_height, current_height):

    current_height += 1

    if not current_height%target_height:
        node.left, node.right = node.right, node.left

    if node.left:    
        swap_node(node.left, target_height, current_height)
    if node.right:
        swap_node(node.right, target_height, current_height)


