# loop based solution based on hackerrank description - two pointers
# one to find the end, the other to find the data.
# 
# the clearest would be a loop to find the length and a loop to find 
# the end, probably what I'd do in real life

def GetNode(head, position):
    
    node_len = head

    for _ in range(position + 1):
        node_len = node_len.next
    
    node_data = head
    while(node_len):
        node_len = node_len.next
        node_data = node_data.next

    return node_data.data
    

