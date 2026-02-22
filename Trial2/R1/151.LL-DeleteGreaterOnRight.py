def compute(self,head):
        #Your code here
        def reverse(head=None):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        head = reverse(head)
        reversed_head = head
        ll_max = head.data
        prev = head
        while head and head.next:
            while head.next and head.next.data < ll_max:
                head = head.next
            prev.next = head.next
            prev = head.next
            head = head.next
            if prev:
                ll_max = max(ll_max, prev.data)