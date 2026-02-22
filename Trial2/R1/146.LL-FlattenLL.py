#https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
import heapq
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.bottom = None
class Cmp:
    def __init__(self, node):
        self.node = node
 
    def __lt__(self, other):
        return self.node.data < other.node.data
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

    def flatten(root):
        pq = []
        while root:
            heapq.heappush(pq, Cmp(root))
            root = root.next
        dummy = Node(0)
        temp = dummy
        
        while pq:
            node = heapq.heappop(pq).node
            temp.bottom = node
            temp = node
            
            if node.bottom:
                heapq.heappush(pq, Cmp(node.bottom))
    
        return dummy.bottom

llist = LinkedList()
nn5 = llist.push(7)
nn4 = llist.push(5)
nn3 = llist.push(7)

res = llist.palindrome(llist.head)
print(res)