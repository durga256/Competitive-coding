def minSwaps(self, n : int, A : List[int]) -> int:
    # code here
    def min_swaps_sort_arr(arr):
        new_arr = arr.copy()
        new_arr.sort()
        i = 0
        res  = 0
        while i < len(arr):
            if arr[i] != new_arr[i]:
                idx = arr.index(new_arr[i])
                arr[idx], arr[i] = arr[i], arr[idx]
                res += 1
            i += 1
        return res
    inorder_arr = []
    def inorder(A, n, index):
        if index >= n:
            return
        
        inorder(A, n, 2*index+1)
        inorder_arr.append(A[index])
        inorder(A, n, 2*index+2)
        
    inorder(A, n, 0)
    #print(inorder_arr)
    return min_swaps_sort_arr(inorder_arr)