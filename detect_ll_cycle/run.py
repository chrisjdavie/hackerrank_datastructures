
def has_cycle(head):
    if not head:
        return False

    tortoise = head
    hare = head

    while(hare and hare.next):
        tortoise = tortoise.next
        hare = hare.next.next
        
        if hare is tortoise:
            has_cycle_b = True
            break
    else:
        has_cycle_b = False

    return has_cycle_b 
