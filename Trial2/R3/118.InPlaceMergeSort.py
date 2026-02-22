def merge(arr,l,mid,h):
    start1 = l
    end1 = mid
    start2 = mid+1
    end2 = h

    if arr[end1] <= arr[start2]:
        return 
    
    while start1 <= end1 and start2 <= end2:
        if arr[start1] <= arr[start2]:
            start1 += 1
        else:
            val = arr[start2]
            idx = start2
            while idx != start1:
                arr[idx] = arr[idx-1]
                idx -= 1
            arr[start1] = val
            start1 += 1; start2 += 1; end1 += 1
def merge_sort(arr, l, h):
    if l < h:
        mid_idx = (h-l)//2+l

        merge_sort(arr,l,mid_idx)
        merge_sort(arr,mid_idx+1,h)

        merge(arr,l,mid_idx, h)

arr = [468,335,1,170,225,479,359,463,465,206,146,282,328,462,492,496,443,328,437,392,105,403,154,293,383,422,217,219,396,448,227,272,39,370,413,168,300,36,395,204,312,323]
merge_sort(arr, 0, len(arr)-1)
print(arr)

        