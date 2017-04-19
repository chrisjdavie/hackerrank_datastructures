
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
    new_node = Node(data)
    if not head:
        return new_node

    next_node = head

    while(next_node):

        if next_node.data >= new_node.data:
            new_node.prev = next_node.prev
            if new_node.prev:            
                new_node.prev.next = new_node
            
            new_node.next = next_node
            next_node.prev = new_node

            if next_node is head:
                head = new_node
            break

        prev_node = next_node
        next_node = next_node.next

    else:
        
        prev_node.next = new_node
        new_node.prev = prev_node

    return head

