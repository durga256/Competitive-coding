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
    
    def remove_duplicates(self, head):
        curr = head
        next = curr.next
        while next:
            while next and curr.data == next.data:
                next = next.next
            curr.next = next
            curr = next
            

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
nn5 = llist.push(8)
nn4 = llist.push(8)
nn3 = llist.push(8)
nn2 = llist.push(7)
nn1 = llist.push(7)

llist.remove_duplicates(llist.head)
llist.printList()
