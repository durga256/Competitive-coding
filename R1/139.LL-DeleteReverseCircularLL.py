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
    
    def deleteNode(self, head, key):
        #your code goes here
        def get_tail(head):
            temp = head
            while temp.next != head:
                temp = temp.next
                
            return temp
        prev = get_tail(head)
        temp = head
        final_head = head
        while temp:
            if temp.data == key:
                if temp == head:
                    final_head = temp.next
                prev.next = temp.next
                return final_head
            prev = temp
            temp = temp.next
            
        return final_head

llist = LinkedList()
nn5 = llist.push(6)
nn4 = llist.push(4)
nn3 = llist.push(8)
nn1 = llist.push(7)
nn1 = llist.push(10)
nn5.next = nn1

tmp = llist.deleteNode(llist.head, 8)
llist.printList(tmp)