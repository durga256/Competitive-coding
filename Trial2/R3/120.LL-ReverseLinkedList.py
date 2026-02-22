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

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_recursive(self,head):
        if head is None or head.next is None:
            return head
        
        rest = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()


        