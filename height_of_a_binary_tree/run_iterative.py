
from queue import Queue

def height(root):

    nodes_remaining = Queue()
    max_height = -1

    nodes_remaining.put((root, 0))

    while(not nodes_remaining.empty()):
        
        current_node, current_height = nodes_remaining.get()

        max_height = max([max_height, current_height])

        if current_node.left:
            nodes_remaining.put((current_node.left, current_height + 1))
        if current_node.right:
            nodes_remaining.put((current_node.right, current_height + 1))

    return max_height

