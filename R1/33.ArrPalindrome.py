#Minimum no. of operations required to make an array palindrome
s = "letelt"

def getInversions(A):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                count += 1
 
    return count


def pal():
    d = {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    
    ideal_pos_list = [-1 for i in range(len(s))]; ideal_tuples = []; mid_ele_idx = -1
    for i in d.keys():
        n = len(d[i])
        for j in range(n//2):
            ideal_tuples.append([d[i][j], d[i][n-1-j]])
        if n % 2 != 0:
            mid_ele_idx = d[i][n//2]

    if mid_ele_idx != -1:
        ideal_pos_list[mid_ele_idx] = len(s)//2

    ideal_tuples.sort()
    for i in ideal_tuples:
        if i[0] == len(s)//2 and mid_ele_idx != -1:
            ideal_pos_list[i[0]] = mid_ele_idx
            ideal_pos_list[i[1]] = len(s)-1-mid_ele_idx
        else:
            ideal_pos_list[i[0]] = i[0]
            ideal_pos_list[i[1]] = len(s)-1-i[0]

    print(ideal_tuples)
    print(ideal_pos_list)
    ans = getInversions(ideal_pos_list)
    print(ans)




pal()
