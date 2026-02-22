#https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
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
    
    def check_circular(self, head=None):
        head = head or self.head
        temp = head
        while temp and temp.next != head:
            temp = temp.next

        if temp and temp.next == head:
            return True
        return False

llist = LinkedList()
nn5 = llist.push(30)
nn4 = llist.push(50)
nn3 = llist.push(10)
nn5 = llist.push(60)
nn4 = llist.push(20)
nn3 = llist.push(40)

tmp = llist.middle_of_linkedlist(llist.head)
llist.printList(tmp)