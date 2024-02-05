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
    
    def palindrome(self, head=None):
        n = self.list_length(head)
        temp = head
        count = 0
        stack = []
        while temp:
            if n%2 and count == n//2:
                pass
            elif count >= n//2:
                if stack[-1] == temp.data:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(temp.data)
            count += 1
            temp = temp.next
        
        return True

llist = LinkedList()
nn5 = llist.push(7)
nn4 = llist.push(5)
nn3 = llist.push(7)

res = llist.palindrome(llist.head)
print(res)