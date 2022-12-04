
def has_cycle(head):
    fast = head;
    slow = head;
    
    while fast and fast.next:
        fast = fast.next.next;
        slow = head.next;
        
        if slow == fast:
            return True;
        
    return False;