
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


