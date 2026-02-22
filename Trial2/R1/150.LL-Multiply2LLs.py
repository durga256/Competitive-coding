#https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
MOD = 10**9+7
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
    
    def multiplyTwoList(self, head1, head2):
        # Code here
        # Challenge - Numbers multiplied directly using their linked lists
        # Not converting to number form - that is more efficient tho
        res = 0
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
    
        multiplier = 1
        original_head2 = head2
        while head1:
            temp_res = 0
            carry = 0
            temp_multiplier = 1
            head2 = original_head2
            while head2:
                temp = (head1.data * head2.data) + carry
                temp_res += (temp%10)*temp_multiplier
                carry = temp //10
                temp_multiplier *= 10
                head2 = head2.next
            while carry:
                temp_res += (carry%10)*temp_multiplier
                carry = carry //10
                temp_multiplier *= 10
            #print(temp_res, head1.data)
            res += temp_res*multiplier
            multiplier *= 10
            head1 = head1.next
            
        return res%MOD
    
num1 = LinkedList()
num1.push(7)
num1.push(1)
num1.push(3)
num1.push(6)
num1.push(8)

num2 = LinkedList()
