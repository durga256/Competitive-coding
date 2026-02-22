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
    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        merged = Node(-1)
        tmp = merged
        while head1 and head2:
            if head1.data <= head2.data:
                tmp.next = head1
                tmp = head1
                head1 = head1.next
            else:
                tmp.next = head2
                tmp = head2
                head2 = head2.next

        while head1:
            tmp.next = head1
            tmp = head1
            head1 = head1.next
        
        while head2:
            tmp.next = head2
            tmp = head2
            head2 = head2.next

        return merged.next

    def merge_sort(self, head):
        if not head.next:
            return head
        
        mid = self.find_mid(head)
        head2 = mid.next
        mid.next = None
        new_head1 = self.merge_sort(head)
        new_head2 = self.merge_sort(head2)
        final_head = self.merge(new_head1, new_head2)
        return final_head  


llist = LinkedList()
nn5 = llist.push(30)
nn4 = llist.push(50)
nn3 = llist.push(10)
nn5 = llist.push(60)
nn4 = llist.push(20)
nn3 = llist.push(40)

tmp = llist.merge_sort(llist.head)
llist.printList(tmp)