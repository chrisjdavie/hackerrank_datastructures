
def has_cycle(node):
    
    has_cycle_b = False
    
    for _ in range(101):
        if not node:
            break
        node = node.next
    else:
        has_cycle_b = True
    
    return has_cycle_b

