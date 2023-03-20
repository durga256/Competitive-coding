# Input: 
# ar1[] = {1, 5, 10, 20, 40, 80} 
# ar2[] = {6, 7, 20, 80, 100} 
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
# Output: 20, 80

# Input: 
# ar1[] = {1, 5, 5} 
# ar2[] = {3, 4, 5, 5, 10} 
# ar3[] = {5, 5, 10, 20} 
# Output: 5, 5

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


def find_common():
    i = j = k = 0
    res = []
    flag = 0
    while i < len(ar1) and j < len(ar2) and k < len(ar3):
        if ar1[i] == ar2[j] == ar3[k]:
            res.append(ar1[i])
            flag = 1
        current_max = max(ar1[i], ar2[j], ar3[k])
        if ar1[i] < current_max:
            i += 1
        if ar2[j] < current_max:
            j += 1
        if ar3[k] < current_max:
            k += 1
        if flag == 1:
            flag = 0
            i += 1; j += 1; k += 1

        
    res = sorted(list(set(res)))# set to remove repeating intersections and sort to send them in ascending
    return res

print(find_common())
