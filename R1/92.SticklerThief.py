arr = [5, 5, 10, 100, 10, 5]
arr = [3,2,7,10]

def f(arr, i, curr_sum):
    excl = 0; incl = 0
    for i in arr:
        new_excl = max(excl, incl) 
        incl = excl+i   #includes arr[i] for upcoming subseq
        excl = new_excl #excludes arr[i] for upcoming subseq
        
    return max(incl, excl)

print(f(arr,0,0))
