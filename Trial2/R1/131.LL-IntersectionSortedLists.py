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
    
    def intersection_sorted_lists(self, head1, head2):
        head = None
        while head1 and head2:
            if head1.data == head2.data:
                if head:
                    new_node = Node(head1.data)
                    head.next = new_node
                    head = new_node
                else:
                    head = Node(head1.data)
                    final_head = head
                head1 = head1.next
                head2 = head2.next
            elif head1.data < head2.data:
                head1 = head1.next
            else:
                head2 = head2.next

        return final_head


llist = LinkedList()
#nn6 = llist.push(6)
nn5 = llist.push(6)
nn4 = llist.push(4)
nn3 = llist.push(3)
nn5 = llist.push(2)
nn4 = llist.push(1)


llist2 = LinkedList()
nn2 = llist2.push(8)
nn1 = llist2.push(6)
nn1 = llist2.push(4)
nn2 = llist2.push(2)

tmp = llist.intersection_sorted_lists(llist.head, llist2.head)
llist.printList(tmp)
