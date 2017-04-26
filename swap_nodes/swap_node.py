from queue import Queue

class Node:

    def __init__(self, data, left = None, right = None):

        self.data = data
        self.left = left
        self.right = right


def swap_node(node, target_height, current_height):

    nodes = Queue()

    nodes.put((node, current_height+1))

    while not nodes.empty():
        node, current_height = nodes.get()

        if not current_height%target_height:
            node.left, node.right = node.right, node.left

        if node.left:
            nodes.put((node.left, current_height+1))
        if node.right:
            nodes.put((node.right, current_height+1))
 
		
