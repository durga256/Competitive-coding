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
    
    def get_tail(self, head):
        while head and head.next:
            head = head.next
        
        return head

    def partition(self, start, end):
        pivot = end
        prev = None
        cur = start
        tail = pivot
        new_head = None
        new_end = None

        while cur != pivot:
            if cur.data < pivot.data:
                if not new_head:
                    new_head = cur
    
                prev = cur
                cur = cur.next
            else:
                if prev: 
                    prev.next = cur.next
                tmp = cur.next
                cur.next = None 
                tail.next = cur
                tail = cur
                cur = tmp
        
        if not new_head:
            new_head = pivot; 
  
        # Update newEnd to the current last node 
        new_end = tail; 
    
        # Return the pivot node 
        return (pivot, new_head, new_end); 

    def quick_sort(self, low, high):
        if not low or low == high or high.next == low:
            return low
        pivot, new_head, new_end = self.partition(low, high)   
        if new_head != pivot:
            # Set the node before the pivot node as NULL 
            tmp = new_head; 
            while tmp.next != pivot:
                tmp = tmp.next; 
            tmp.next = None; 
            # Recur for the list before pivot 
            new_head = self.quick_sort(new_head, tmp); 
    
            # Change next of last node of the left half to 
            # pivot 
            
            tmp = self.get_tail(new_head); 
            tmp.next = pivot
  
        # Recur for the list after the pivot element 
        pivot.next = self.quick_sort(pivot.next, new_end); 
    
        return new_head



llist = LinkedList()
nn5 = llist.push(30)
nn4 = llist.push(50)
nn3 = llist.push(10)
nn5 = llist.push(60)
nn4 = llist.push(20)
nn3 = llist.push(40)

tmp = llist.quick_sort(llist.head, llist.get_tail(llist.head))
llist.printList(tmp)