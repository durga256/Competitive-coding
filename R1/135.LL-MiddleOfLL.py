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
    
    def middle_of_linkedlist(self, head=None):
        temp = head or self.head
        slow = temp
        fast = temp
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

llist = LinkedList()
nn5 = llist.push(30)
nn4 = llist.push(50)
nn3 = llist.push(10)
nn5 = llist.push(60)
nn4 = llist.push(20)
nn3 = llist.push(40)

tmp = llist.middle_of_linkedlist(llist.head)
llist.printList(tmp)