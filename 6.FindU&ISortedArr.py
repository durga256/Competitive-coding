lst1 = [-75,-35,-27,-7,-6,-5,0,4,56]
lst2 = [-99, -78, -7,0, 2, 3, 43,]

index_lst1 = index_lst2 = 0
result = []

#union
#O(n1+n2)
while index_lst1 < len(lst1) and index_lst2 < len(lst2):
    if lst1[index_lst1] < lst2[index_lst2]:
        result.append(lst1[index_lst1])
        index_lst1 += 1
    elif lst1[index_lst1] > lst2[index_lst2]:
        result.append(lst2[index_lst2])
        index_lst2 += 1
    elif lst1[index_lst1] == lst2[index_lst2]:
        result.append(lst1[index_lst1])
        result.append(lst2[index_lst2])
        index_lst1 += 1
        index_lst2 += 1

print(result)

#intersection
#O(n1+n2)
index_lst1 = index_lst2 = 0
result = []

while index_lst1 < len(lst1) and index_lst2 < len(lst2):
    if lst1[index_lst1] == lst2[index_lst2]:
        result.append(lst1[index_lst1])
        index_lst1 += 1
        index_lst2 += 1
    if lst1[index_lst1] < lst2[index_lst2]:
        index_lst1 += 1
    if lst1[index_lst1] > lst2[index_lst2]:
        index_lst2 += 1


print(result)