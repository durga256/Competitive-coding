class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_LL(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("")

def reverse_LL_iter(head):
    prev = None
    next = head
    curr = head
    while next:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def reverse_LL_recur(head):
    if head is None or head.next is None:
        return head
    
    rest = reverse_LL_recur(head.next)

    head.next.next = head

    head.next = None

    return rest

def reverse_LL_stack(head):
    list = []
    while head:
        list.append(head)
        head = head.next

    head = list.pop()
    tail = head
    while list:
        tail.next = list.pop()
        tail = tail.next
        tail.next = None

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print_LL(head)
    head = reverse_LL_iter(head)
    print_LL(head)
    head = reverse_LL_stack(head)
    print_LL(head)

main()