l = [1,5,3,4,2]

#naive solution
# time complexity O(n)
i = 0
j = len(l)-1

print(l)
while i < j:
    l[i], l[j] = l[j], l[i]
    i+=1
    j-=1

print (l)