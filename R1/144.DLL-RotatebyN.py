import heapq
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        return new_node

    def reverse(self, head=None):
        prev = None
        current = head or self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
    
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
    
    def get_tail(self, head):
        while head.next:
            head = head.next

        return head
    
    def rotate_by_n(self, head, n):
        tail = self.get_tail(head)
        tail.next = head
        head.prev = tail
        count = 0
        while count < n-1:
            head = head.next
            count += 1

        head.next.prev = None
        final_head = head.next
        head.next = None
        return final_head

        



llist = LinkedList()
nn7 = llist.push(7)
nn6 = llist.push(6)
nn5 = llist.push(5)
nn5 = llist.push(4)
nn3 = llist.push(3)
nn2 = llist.push(2)
nn1 = llist.push(1)

llist.printList()
print()
tmp = llist.rotate_by_n(llist.head, 2)
llist.printList(tmp)