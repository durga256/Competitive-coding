arr = [1000, 11, 445, 1, 330, 3000]

def f(arr,l,h):
    if l >= h:
        return (arr[l], arr[l])
    if l == h-1:
        return (max(arr[l], arr[h]),min(arr[l],arr[h]))
    else:
        mid = (l+h)//2
        max_ele_1, min_ele_1 = f(arr, l,mid)
        max_ele_2, min_ele_2 = f(arr, mid+1,h)
        return(max(max_ele_1, max_ele_2), min(min_ele_1,min_ele_2))
    
print(f(arr,0,len(arr)-1))