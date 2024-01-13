arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]

def f2():
    arr.sort(key= lambda x:-bin(x)[2:].count('1'))
    print(arr)
f2()

def f():
    count_arr = []
    for i in range(21):
        count_arr.append([])

    for i in range(len(arr)):
        set_bit_count = bin(arr[i]).count('1')
        count_arr[set_bit_count].append(arr[i])

    k = 0
    for i in range(len(count_arr)-1,-1,-1):
        for j in count_arr[i]:
            arr[k] = j
            k += 1

    print(arr)

f()
