#https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
#https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
grid = ["GEEKSFORGEEKS","GEEKSQUIZGEEK","IDEQAPRACTICE"]
word = "EE"; ans = []

def find_diag():
    m = len(word)
    r = len(grid); c = len(grid[0]); diag = []
    #column diag
    for i in range(1,r):
        if r - i >= m:
            k = 0; res = ""
            for j in range(i,r):
                res += grid[j][k]
                k += 1
            diag.append([res, "R"+str(i)])

    #row diag
    for i in range(c-m+1):
        k = 0; res = ""
        for j in range(i,c):
            if k >= r:
                break
            res += grid[k][j]
            k += 1
        diag.append([res,"C"+str(i)])

    return diag

def rabin_karp(haystack, needle_hashf, needle_hashb, needle, c):
    m = len(needle)
    hay_hashf = 0; hay_hashb = 0

    if m > len(haystack):
        return

    for i in range(m):
        hay_hashf += (ord(haystack[i])  - 64) * (26 ** (m-i-1))
        hay_hashb += (ord(haystack[i])  - 64) * (26 ** i)

    if hay_hashf == needle_hashf:
        if c[0] == "R":
            c = int(c[1:])
            c = "row=" + str(c)
        elif c[0] == "C":
            c = int(c[1:])
            c = "col=" + str(c)
        ans.append([0, c])
    elif hay_hashf == needle_hashb and needle_hashf != needle_hashb:
        if c[0] == "R":
            c = int(c[1:])
            c = "row=" + str(c+m)
        elif c[0] == "C":
            c = int(c[1:])
            c = "col=" + str(c+m)
        ans.append([m, c])

    for i in range(len(haystack)-m):
        hay_hashf -= (ord(haystack[i])  - 64) * (26 ** (m-1))
        hay_hashf *= 26
        hay_hashf += (ord(haystack[i+m])  - 64)

        # hay_hashb -= (ord(haystack[i])  - 64)
        # hay_hashb /= 26
        # hay_hashb += (ord(haystack[i+m])  - 64) * (26 ** (m-1))

        if hay_hashf == needle_hashf:
            if c[0] == "R":
                c = int(c[1:])
                c = "row=" + str(c+i+1)
            elif c[0] == "C":
                c = int(c[1:])
                c = "col=" + str(c+i+1)
            ans.append([i+1,c])
        elif hay_hashf == needle_hashb and needle_hashf != needle_hashb:
            if c[0] == "R":
                c = int(c[1:])
                c = "row=" + str(c+i+1)
            elif c[0] == "C":
                c = int(c[1:])
                c = "col=" + str(c+i+1)
            ans.append([i+m,c])


def find():
    diag = find_diag()
    #print(diag)
    m = len(word)
    r = len(grid); c = len(grid[0])
    needle_hashf = needle_hashb = 0
    for i in range(m):
        needle_hashf += (ord(word[i])  - 64) * (26 ** (m-i-1))
        needle_hashb += (ord(word[i])  - 64) * (26 ** i)

    for i in range(r):
        rabin_karp(grid[i], needle_hashf, needle_hashb, word, "row="+str(i))

    #print("horizontal done")

    for i in range(c):
        haystack = ""; k = 0
        while k < r:
            haystack += grid[k][i]
            k += 1
        rabin_karp(haystack, needle_hashf, needle_hashb, word, "col="+str(i))

    #print("Vertical done")



    for i in diag:
        rabin_karp(i[0], needle_hashf, needle_hashb, word, i[1])

    for i in ans:
        print(i)   
    

find()
            


