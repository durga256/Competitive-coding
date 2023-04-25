#Minimum swaps required bring elements less equal K together
import sys

arr = [2, 7, 9, 5, 8, 7, 4]; k = 5
#arr = [7,9,5,8,2,4]; k = 5
arr = [2,1,5,6,3]; k = 3
arr = [20,12,17]; k = 6
#arr = [10,12,20,20,5,19,19,12,1,20,1]; k = 1
arr = [4,16,3,8,13,2,19,4,12,2,7,17,4,19,1]; k = 9

def min_swap():
    cnt_lessk = 0
    for i in range(len(arr)):
        if arr[i] <= k:
            cnt_lessk += 1

    low = 0; high = cnt_lessk -1; bad = 0
    while low <= high:
        if arr[low] > k:
            bad += 1
        low += 1
    min_bad = bad
    print(min_bad)
    for i in range(len(arr)-cnt_lessk):
        if arr[i] > k and arr[i+cnt_lessk] <= k:
            bad -= 1
        if arr[i] <= k and arr[i+cnt_lessk] > k:
            bad += 1
        min_bad = min(min_bad,bad)
        if i == 1:
            print(min_bad, bad)
            print(arr[i], arr[i+cnt_lessk])
    return min_bad



print("ans: ",min_swap())