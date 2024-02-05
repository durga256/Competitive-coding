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
    
    def add_1_to_ll(self):
        last_non_nine = -1
        temp_head = self.head
        count = 0
        while temp_head:
            if temp_head.data != 9:
                last_non_nine = count
            temp_head = temp_head.next
            count += 1

        list_len = count
        if last_non_nine == -1:
            temp = Node(1)
            temp.next = self.head
            return temp
        
        count = 0
        temp_head = self.head
        while temp_head and count < last_non_nine:
            temp_head = temp_head.next
            count += 1

        temp_head.data += 1
        temp_head = temp_head.next
        while temp_head:
            temp_head.data = 9
            temp_head = temp_head.next


        

        


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
nn5 = llist.push(5)
nn4 = llist.push(4)
nn3 = llist.push(3)
nn2 = llist.push(2)
nn1 = llist.push(1)

llist.printList()
tmp = llist.add_1_to_ll()
print('')
llist.printList(tmp)
