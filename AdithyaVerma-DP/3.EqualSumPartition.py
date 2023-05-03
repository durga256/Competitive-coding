arr = [1,5,11,5,4]
def sub(arr, n, c):
    if n == 0:
        return False
    if c == 0:
        return True
    return sub(arr,n-1,c-arr[n-1]) or sub(arr, n-1, c)

def find():
    sum_arr = sum(arr)
    if sum_arr % 2 != 0:
        return False
    return sub(arr,len(arr),sum_arr/2)

print(find())
