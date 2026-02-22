arr = [64, 25, 12, 22, 11]

def main():
    n = len(arr)

    for i in range(n):
        smallest_idx = i
        for j in range(i+1, n):
            if arr[smallest_idx] > arr[j]:
                smallest_idx = j
        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]

    print(arr)

main()
