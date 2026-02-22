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
    
    def split_circular(self, head=None):
        if not head:
            return head, None
        slow = head
        fast = head
        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        if fast.next == head:
            fast.next = slow.next
        else:
            fast.next.next = slow.next
        slow.next = head
            
        #this is to emulate pass by reference in python please don't delete below line.
        return (head1,head2)


llist = LinkedList()
nn5 = llist.push(7)
nn4 = llist.push(5)
nn3 = llist.push(1)
#nn2 = llist.push(2)
nn5.next = nn3

tmp1, tmp2 = llist.split_circular(llist.head)
llist.printList(tmp1)
print('')
llist.printList(tmp2)