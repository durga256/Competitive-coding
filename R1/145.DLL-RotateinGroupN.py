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

    def printList_backwards(self, head=None):
        temp = head or self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.prev

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
    
    def rotate_in_group_n(self, head, n):
        prev_head = None
        count = n
        next = head
        while head:
            while head and next and count:
                if count == n:
                    old_head = head
                next = head.next
                head.next, head.prev = head.prev, head.next
                count -= 1
                if count and next:
                    head = next
            if not prev_head:
                final_head = head
            if head:
                if prev_head:
                    prev_head.next = head
                head.prev = prev_head
                prev_head = old_head
            old_head.next = next
            count = n
            head = next

        return final_head

llist = LinkedList()
nn8 = llist.push(8)
nn7 = llist.push(7)
nn6 = llist.push(6)
nn5 = llist.push(5)
nn5 = llist.push(4)
nn3 = llist.push(3)
nn2 = llist.push(2)
nn1 = llist.push(1)

llist.printList()
print()
tmp = llist.rotate_in_group_n(llist.head, 3)
llist.printList(tmp)
print()
llist.printList_backwards(llist.get_tail(tmp))
