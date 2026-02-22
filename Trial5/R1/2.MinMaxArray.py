arr = [1,45,6,71,89,9]

# O(n) space-O(1)
def iter_min_max():
    min_ele = arr[0]
    max_ele = arr[0]

    for i in range(len(arr)):
        if arr[i] < min_ele:
            min_ele = arr[i]
        # Scenario this breaks would be if all elements are same but
        # we took care of that with assigning arr[0] as initial answers
        elif arr[i] > max_ele:
            max_ele = arr[i]

    return min_ele, max_ele

#O(n) space - O(1)
def python_min_max():
    return min(arr), max(arr)

print(iter_min_max())
print(python_min_max())


