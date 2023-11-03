ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]

def medians_2arrs():
    n = len(ar1); m = len(ar2)

    i = j = 0; res = 0
    if (n+m)%2 == 0:
        while i < n and j < m:
            if ar1[i] < ar2[j]:
                if i+j == (n+m)/2 or i+j == ((n+m)/2)-1:
                    res += ar1[i]
                i += 1
            else:
                if i+j == (n+m)/2 or i+j == ((n+m)/2)-1:
                    res += ar2[j]
                j += 1
        res = res // 2
    else:
        while i < n and j < m:
            if ar1[i] < ar2[j]:
                if i+j == (n+m)//2:
                    res += ar1[i]
                i += 1
            else:
                if i+j == (n+m)//2:
                    res += ar2[j]
                j += 1

    print(res)

medians_2arrs()

def med_2arrs_binary_search():
    l1 = l2 = 0; h1 = h2 = len(ar1) - 1
    while h1 - l1 > 1 and h2 - l2 > 1:
        mid1 = (h1-l1)//2+l1
        mid2 = (h2-l2)//2+l2

        if ar1[mid1] == ar2[mid2]:
            return ar1[mid1]
        elif ar1[mid1] > ar2[mid2]:
            h1 = mid1; l2 = mid2
        else:
            h2 = mid2; l1 = mid1

    res = (max(ar1[l1], ar2[l2])+min(ar1[h1], ar2[h2]))//2
    print(res)

med_2arrs_binary_search()
