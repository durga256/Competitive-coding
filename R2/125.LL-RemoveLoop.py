#https://leetcode.com/problems/reverse-nodes-in-k-group/
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def remove_loop(self, head):
        slow_p = head
        fast_p = head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
            if slow_p == fast_p:
                slow_p = head
                # if head is the node next to link node i.e,, the linked list is a circle
                if slow_p == fast_p:
                    while (fast_p.next != slow_p):
                        fast_p = fast_p.next
                else:
                    while slow_p.next != fast_p.next:
                        slow_p = slow_p.next
                        fast_p = fast_p.next
                fast_p.next = None
                return
            

    def printList(self, head=None):
        temp = head or self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

    def list_length(self, head=None):
        temp = head or self.head
        res = 0
        while temp != None:
            res += 1
            temp = temp.next
        return res


llist = LinkedList()
#nn6 = llist.push(6)
nn5 = llist.push(16)
nn4 = llist.push(34)
nn3 = llist.push(36)
nn2 = llist.push(58)
nn1 = llist.push(7)

nn5.next = nn1
llist.remove_loop(llist.head)
llist.printList()
