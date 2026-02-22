class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    while head:
        print(head.data, end="->")
        head = head.next

    print()

def reverse_given_size(head, k):
    prev = None
    curr = next = head
    prev_tail = None
    new_head = None
    while next:
        temp_k = k
        while next and temp_k:
            if temp_k == k:
                next_tail = curr
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            temp_k -= 1
        if not new_head:
            new_head = prev
        else:
            prev_tail.next = prev
        prev_tail = next_tail
    prev_tail.next = None

    return new_head

def reverse_k_nodes(head, k):
    curr = next = head
    prev = None
    while next and k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        k -= 1

    return prev

def reverse_given_size_recur(head, k):
    if not head or not head.next:
        return head
    
    temp = head
    temp_k = k
    while temp and temp_k:
        temp = temp.next
        temp_k -= 1
    
    if temp_k != 0:
        return head
    else:
        groupHead = reverse_k_nodes(head, k)
        head.next = reverse_given_size_recur(temp, k)

    return groupHead

def reverse_given_size_stack(head, k):
    new_head = None
    stack = []
    while head:
        temp_k = k
        while head and temp_k:
            stack.append(head)
            head = head.next
            temp_k -= 1
        prev_node = None
        while stack:
            node = stack.pop()
            if not new_head:
                new_head = node
            if stack:

            

        
        
            

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverse_given_size_recur(head, 2)
    print_list(head)
main()