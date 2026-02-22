class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def count_inversions(self,arr):
        if len(arr) > 1:
            mid_idx = len(arr)//2
    
            L = arr[:mid_idx]
            R = arr[mid_idx:]
    
            self.count_inversions(L)
            self.count_inversions(R)
    
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    self.ans += len(L) - i
                k += 1
    
            while i < len(L):
                arr[k] = L[i]
                i += 1; k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1; k += 1

    def inversionCount(self, arr, n):
        self.ans = 0
        self.count_inversions(arr)
        return self.ans