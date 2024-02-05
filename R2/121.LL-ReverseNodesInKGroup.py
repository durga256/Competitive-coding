#https://leetcode.com/problems/reverse-nodes-in-k-group/
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

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def reverseKGroup(self, head, k, n):
        dummy_node = Node(-1)

        prev = head
        curr = head
        next = head
        temp_k = k
        flag = True
        final_head = dummy_node
        while curr and n//k >= 1:
            while curr and temp_k != 0:
                if temp_k == k:
                    next_head = curr
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                temp_k -= 1
            n -= k
            if flag:
                final_head = prev
                flag = False
            dummy_node.next = prev
            next_head.next = None
            dummy_node = next_head
            temp_k = k
        return final_head

    def reverse_recursive(self,head):
        if head is None or head.next is None:
            return head
        
        rest = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

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
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print ("Given linked list")
#llist.printList()
# tmp = llist.reverseKGroup(llist.head, 2)
# print ("\nReversed linked list")
n = llist.list_length()
tmp = llist.reverseKGroup(llist.head, 2, n)
print ("\nReversed linked list")
llist.printList(tmp)

#Creates a new list. Faster but not what is required
class Solution:
    def reverseKGroup(self, head, k: int):
        lst=[]
        tmp=head
        while tmp:
            lst.append(tmp.val)
            tmp=tmp.next
        res=[]
        for i in range(0,len(lst),k):
            t=lst[i:i+k]
            if len(t)==k:
                res+=t[::-1]
            else:
                res+=t
        dummy=Node(0)
        temp=dummy
        while len(res)!=0:
            temp.next=Node(res.pop(0))
            temp=temp.next
        return dummy.next
        