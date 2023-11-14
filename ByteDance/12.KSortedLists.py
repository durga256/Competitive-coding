# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def push_to_list(self, head, data):
        tmp = ListNode(data)
        while head.next:
            head = head.next

        head.next = tmp

    def merge_linked_lists(self, h1,h2):
        res_head = ListNode(0)
 
        res = res_head
        while True:
            if h1 is None:
                res.next = h2
                break
            if h2 is None:
                res.next = h1
                break
            if h1.val <= h2.val:
                res.next = h1
                h1= h1.next
            else:
                res.next = h2
                h2 = h2.next
            
            res = res.next
        return res_head.next
    
    def print_list(self,head):
        while head:
            print(head.val,end="->")
            head = head.next
        print("")

    def mergeKLists(self, lists):
        temp_lists = []
        for i in range(len(lists)):
            if lists[i]:
                temp_lists.append(lists[i])
        lists = temp_lists
        if lists:
            res = lists[0]
            for i in range(1,len(lists)):
                if res and lists[i]:
                    res = self.merge_linked_lists(res, lists[i])
            
            return res

sol = Solution()
head1 = ListNode(1) #145
head2 = ListNode(1) #134
head3 = ListNode(2) #26
sol.push_to_list(head1, 4)
sol.push_to_list(head1, 5)
sol.push_to_list(head2,3)
sol.push_to_list(head2, 4)
sol.push_to_list(head3, 6)
lists = [head1,head2, head3]
sol.print_list(sol.mergeKLists(lists))

