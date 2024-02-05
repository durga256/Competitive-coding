class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
def copyList(self, head):
        # code here
        temp = head
        while temp:
            new_node = Node(temp.data)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
            
        temp = head
        new_head = head.next
        while temp:
            if temp.arb:
                temp.next.arb = temp.arb.next
            temp = temp.next.next
            
        temp = head
        while temp:
            next = temp.next.next
            if temp.next.next:
                temp.next.next = temp.next.next.next
            temp.next = next
            temp = next
            
        return new_head