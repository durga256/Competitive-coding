#https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
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
    def find_sum(self, head, key):
        temp = head
        res = []
        while temp.next:
            temp_key = key - temp.data
            first = temp.next
            last  = self.get_tail(head)
            while first != last and last.next != first:
                print(temp_key, first.data, last.data)
                if first.data + last.data == temp_key:
                    res.append((temp.data, first.data, last.data))
                    first = first.next
                    last = last.prev
                else:
                    if first.data + last.data < temp_key:
                        first = first.next
                    else:
                        last = last.prev
            temp = temp.next

        return res

llist = LinkedList()
nn7 = llist.push(9)
nn6 = llist.push(8)
nn5 = llist.push(6)
nn5 = llist.push(5)
nn3 = llist.push(4)
nn2 = llist.push(2)
nn1 = llist.push(1)

tmp = llist.find_sum(llist.head, 7)
print(tmp)