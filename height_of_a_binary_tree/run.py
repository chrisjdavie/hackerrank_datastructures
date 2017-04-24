
from queue import Queue

def height(root, current_height = -1):

    max_height = current_height

    if root:
        max_height += 1
        max_height = max([height(root.left, max_height),
                          height(root.right, max_height)])

    return max_height

