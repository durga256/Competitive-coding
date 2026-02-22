arr = [90,7,8,98,45,54,35]

def find_min_max(a):
    min_ele = a[0]; max_ele = a[0]
    for i in a:
        if i > max_ele:
            max_ele = i
        if i < min_ele:
            min_ele = i

    return {
        "min_ele": min_ele,
        "max_ele": max_ele}

print(find_min_max(arr))