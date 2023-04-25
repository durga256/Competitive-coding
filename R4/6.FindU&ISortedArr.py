#find union and intersection of 2 sorted arrs
lst1 = [-75,-35,-27,-7,-6,-5,0,4,56]
lst2 = [-99, -78, -7,0, 2, 3, 43]
res_union = []
res_intersection = []

def find_union():
    i = 0; j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            res_union.append(lst1[i])
            i += 1
            j += 1
        if lst1[i] < lst2[j]:
            res_union.append(lst1[i])
            i += 1
        if lst2[j] < lst1[i]:
            res_union.append(lst2[j])
            j += 1
    while i < len(lst1):
        res_union.append(lst1[i])
        i += 1
    while j < len(lst2):
        res_union.append(lst2[j])
        j += 1
    print(res_union)

def find_intersection():
    i = 0; j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            res_intersection.append(lst1[i])
            i += 1
            j += 1
        if lst1[i] < lst2[j]:
            i += 1
        if lst2[j] < lst1[i]:
            j += 1
    
    print(res_intersection)


find_union()
find_intersection()
