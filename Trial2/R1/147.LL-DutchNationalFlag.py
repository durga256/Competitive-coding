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
    def count_chars(self, head, char):
        res = 0
        while head:
            if head.data == char:
                res += 1
            head = head.next
        
        return res

    def dutch_national(self, head):
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)

        zero_prev = zero_dummy
        one_prev = one_dummy
        two_prev = two_dummy

        temp = head
        while temp:
            next = temp.next
            if temp.data == 0:
                zero_prev.next = temp
                temp.next = None
                zero_prev = temp
            elif temp.data == 1:
                one_prev.next = temp
                temp.next = None
                one_prev = temp
            else:
                two_prev.next = temp
                temp.next = None
                two_prev = temp
            temp = next

        zero_prev.next = one_dummy.next
        one_prev.next = two_dummy.next
        head = zero_dummy.next
        return head



llist = LinkedList()
nn5 = llist.push(1)
nn4 = llist.push(0)
nn3 = llist.push(2)
nn3 = llist.push(0)
nn3 = llist.push(2)
nn3 = llist.push(1)
nn3 = llist.push(1)

tmp = llist.dutch_national(llist.head)
llist.printList(tmp)