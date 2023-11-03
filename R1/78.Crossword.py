grid = ["GEEKSFORGEEKS",
        "GEEKSQUIZGEEK",
        "IDEQAPRACTICE"]
word = "EE"; ans = []

def find_diag():
    m = len(word)
    r = len(grid); c = len(grid[0]); diag = []

    for i in range(1,r):
        if r-i >= m:
            k = 0; res = ""
            for j in range(i,r):
                res += grid[j][k]
                k += 1
            diag.append([res, 'R'+str(i)])

    for i in range(c-m+1):
        k = 0; res = ""
        for j in range(i,c):
            if k >= r:
                break
            res += grid[k][j]
            k += 1
        diag.append([res, 'C'+str(i)])

    return diag

def rabin_karp(haystack, m, needle_hashf, needle_hashb, idx_info):
    
    haystack_hashf = 0
    if m > len(haystack):
        return
    for i in range(m):
        haystack_hashf += (ord(haystack[i])-64)*(26**(m-i-1))

    if haystack_hashf == needle_hashf:
        if idx_info[0] == 'R':
            idx_info = int(idx_info[1:])
            idx_info = "row=" + str(idx_info)
        elif idx_info[0] == 'C':
            idx_info = int(idx_info[1:])
            idx_info = "col=" + str(idx_info)
        ans.append([0,idx_info])
    elif haystack_hashf == needle_hashb and needle_hashb != needle_hashf:
        if idx_info[0] == 'R':
            idx_info = int(idx_info[1:])
            idx_info = "row=" + str(idx_info+m)
        elif idx_info[0] == 'C':
            idx_info = int(idx_info[1:])
            idx_info = "col=" + str(idx_info+m)
        ans.append([m,idx_info])

    for i in range(len(haystack)-m):
        haystack_hashf -= (ord(haystack[i])-64)*(26**(m-1))
        haystack_hashf *= 26
        haystack_hashf += (ord(haystack[i+m])-64)

        if haystack_hashf == needle_hashf:
            if idx_info[0] == 'R':
                idx_info = int(idx_info[1:])
                idx_info = "row=" + str(idx_info+i)
            elif idx_info[0] == 'C':
                idx_info = int(idx_info[1:])
                idx_info = "col=" + str(idx_info+i)
            ans.append([i+1,idx_info])
        elif haystack_hashf == needle_hashb and needle_hashb != needle_hashf:
            if idx_info[0] == 'R':
                idx_info = int(idx_info[1:])
                idx_info = "row=" + str(idx_info+i+1)
            elif idx_info[0] == 'C':
                idx_info = int(idx_info[1:])
                idx_info = "col=" + str(idx_info+i)
            ans.append([i+m,idx_info])

def f():
    m = len(word)
    r = len(grid); c = len(grid[0])
    needle_hashf = 0
    needle_hashb = 0

    for i in range(m):
        needle_hashf += (ord(word[i])-64)*(26**(m-i-1))
        needle_hashb += (ord(word[i])-64)*(26**i)

    for i in range(r):
        rabin_karp(grid[i], len(word), needle_hashf,needle_hashb, 'R'+str(i))

    for i in range(c):
        k = ""
        for j in range(r):
            k += grid[j][i]
        rabin_karp(k, len(word), needle_hashf,needle_hashb, 'C'+str(i))

    diag = find_diag()
    for i in diag:
        rabin_karp(i[0], len(word), needle_hashf,needle_hashb, i[1])

    for i in ans:
        print(i)

f()
