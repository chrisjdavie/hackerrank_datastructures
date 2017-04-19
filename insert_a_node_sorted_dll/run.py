
class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    @classmethod
    def build_from_list(obj, data):
        
        head = obj(data[0])
        prev_node = head        
        
        for value in data[1:]:
            new_node = obj(value, prev_node = prev_node)
            prev_node.next = new_node
            prev_node = new_node

        return head


def SortedInsert(head, data):

    prev_node = None
    next_node = head

    while(next_node and next_node.data < data):
        prev_node = next_node
        next_node = next_node.next

    new_node = Node(data)

    new_node.prev = prev_node
    if prev_node:
        prev_node.next = new_node
    else:
        head = new_node

    new_node.next = next_node
    if next_node:
        next_node.prev = new_node

    return head

