arr = [90,7,8,98,45,54,35]

def rot_arr():
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = temp
    print(arr)

rot_arr()