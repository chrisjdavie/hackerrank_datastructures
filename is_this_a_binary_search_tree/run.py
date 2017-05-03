from queue import Queue

def check_binary_search_tree_(head):

    lower_bound = -1
    upper_bound = 10**4 + 1

    is_binary_search_tree = True

    nodes_to_check = Queue()

    nodes_to_check.put((head, lower_bound, upper_bound))

    while not nodes_to_check.empty():
        
        node, lower_bound, upper_bound = nodes_to_check.get()
        if node.data <= lower_bound or node.data >= upper_bound:
            is_binary_search_tree = False
            break

        if node.left:
            nodes_to_check.put((node.left, lower_bound, node.data))
        if node.right:
            nodes_to_check.put((node.right, node.data, upper_bound))

    return is_binary_search_tree

