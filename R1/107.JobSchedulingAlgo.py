import heapq
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,arr,n):
        arr.sort(key=lambda x: x.deadline)

        maxheap = []
    
        result = 0; total_profit = 0
        for i in range(n-1,-1,-1):
    
            if i == 0:
                slots_left = arr[i].deadline
            else:
                slots_left = arr[i].deadline - arr[i-1].deadline
    
            heapq.heappush(maxheap, (-arr[i].profit, arr[i].deadline))
    
            
            while maxheap and slots_left:
                profit, deadline = heapq.heappop(maxheap)
    
                slots_left -= 1
    
                result += 1
                total_profit += -profit
    
        return [result, total_profit]