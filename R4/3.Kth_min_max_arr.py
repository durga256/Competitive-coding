arr = [90,7,8,98,45,54,35]


def sort_arr(a):
    a = sorted(a)
    return a

def get_kth_min_max(a, k):
    return {
        "kth min": a[k-1],
        "kth max": a[len(a)-k]
    }

arr = sort_arr(arr)
print(get_kth_min_max(arr,3))