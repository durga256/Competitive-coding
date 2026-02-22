# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge_2_lls(self, h1, h2):
        dummy_node = ListNode(-1)
        tail = dummy_node
        while True:
            if not h1:
                tail.next = h2
                break
            if not h2:
                tail.next = h1
                break
            if h1.val <= h2.val:
                tail.next = h1
                tail = h1
                h1 = h1.next
            else:
                tail.next = h2
                tail = h2
                h2 = h2.next

        return dummy_node.next
    def mergeKLists(self, lists):
        temp_lists = []
        for i in lists:
            if i:
                temp_lists.append(i)

        if temp_lists:
            res = temp_lists[0]
            for i in range(1,len(temp_lists)):
                if res and temp_lists[i]:
                    res = self.merge_2_lls(res, temp_lists[i])
                    print(res.val)

            return res
        
class CustomListNode:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists):
        heap = [CustomListNode(i) for i in lists if i]
        heapq.heapify(heap)
        dummy_node = ListNode(-1)
        temp = dummy_node
        while heap:
            node = heapq.heappop(heap).node
            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(heap, CustomListNode(node.next))

        return dummy_node.next
        

        