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
    
    def add_2_nums(self, head1, head2):
        tmp1 = self.list_length(head1)
        tmp2 = self.list_length(head2)
        if tmp1 < tmp2:
            head1, head2 = head2, head1
        head1 = self.reverse(head1)
        final_head1 = head1
        head2 = self.reverse(head2)
        carry = 0
        while head1 and head2:
            temp = head1.data + head2.data + carry
            head1.data = temp%10
            carry = temp // 10
            print(temp, head1.data, carry)
            end_of_head1 = head1
            head1 = head1.next
            head2 = head2.next

        while head1:
           temp =  head1.data + carry
           head1.data = temp%10
           carry = temp //10
           end_of_head1 = head1
           head1 = head1.next


        while carry:
            new_node = Node(carry%10)
            carry = carry //10
            end_of_head1.next = new_node
            end_of_head1 = new_node

        final_head1 = self.reverse(final_head1)
        return final_head1




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
nn5 = llist.push(4)
nn4 = llist.push(9)
nn3 = llist.push(6)
nn5 = llist.push(3)
nn4 = llist.push(8)
nn3 = llist.push(7)
nn5 = llist.push(1)


llist2 = LinkedList()
nn2 = llist2.push(3)
nn1 = llist2.push(8)
nn1 = llist2.push(3)
nn2 = llist2.push(2)
nn1 = llist2.push(7)
nn1 = llist2.push(5)
nn2 = llist2.push(8)
nn1 = llist2.push(4)
nn1 = llist2.push(8)

tmp = llist.add_2_nums(llist.head, llist2.head)
llist.printList(tmp)
